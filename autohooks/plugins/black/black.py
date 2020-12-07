# Copyright (C) 2019 Greenbone Networks GmbH
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import subprocess

from autohooks.api import ok, error
from autohooks.api.git import (
    get_staged_status,
    stage_files_from_status_list,
    stash_unstaged_changes,
)
from autohooks.api.path import match

DEFAULT_INCLUDE = ('*.py',)
DEFAULT_ARGUMENTS = ('-q',)


def check_black_installed():
    try:
        import black  # pylint: disable=unused-import, import-outside-toplevel
    except ImportError:
        raise Exception(
            'Could not find black. '
            'Please add black to your python environment.'
        ) from None


def get_black_config(config):
    return config.get('tool', 'autohooks', 'plugins', 'black')


def ensure_iterable(value):
    if isinstance(value, str):
        return [value]
    return value


def get_include_from_config(config):
    if not config:
        return DEFAULT_INCLUDE

    black_config = get_black_config(config)
    include = ensure_iterable(
        black_config.get_value('include', DEFAULT_INCLUDE)
    )

    return include


def get_black_arguments(config):
    if not config:
        return DEFAULT_ARGUMENTS

    black_config = get_black_config(config)
    arguments = ensure_iterable(
        black_config.get_value('arguments', DEFAULT_ARGUMENTS)
    )

    return arguments


def precommit(config=None, **kwargs):  # pylint: disable=unused-argument
    check_black_installed()

    include = get_include_from_config(config)
    files = [f for f in get_staged_status() if match(f.path, include)]

    if len(files) == 0:
        ok('No staged files for black available.')
        return 0

    arguments = ['black']
    arguments.extend(get_black_arguments(config))

    with stash_unstaged_changes(files):
        for f in files:
            try:
                args = arguments.copy()
                args.append(str(f.absolute_path()))

                subprocess.check_call(args)
                ok('Running black on {}'.format(str(f.path)))
            except subprocess.CalledProcessError as e:
                error('Running black on {}'.format(str(f.path)))
                raise e from None

        stage_files_from_status_list(files)

    return 0
