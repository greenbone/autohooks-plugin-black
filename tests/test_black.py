# Copyright (C) 2020-2022 Greenbone AG
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

import sys
from pathlib import Path
from unittest import TestCase
from unittest.mock import patch

from autohooks.api.git import StatusEntry
from autohooks.config import load_config_from_pyproject_toml

from autohooks.plugins.black.black import (
    DEFAULT_ARGUMENTS,
    DEFAULT_INCLUDE,
    check_black_installed,
    ensure_iterable,
    get_black_arguments,
    get_black_config,
    get_include_from_config,
    precommit,
)


def get_test_config_path(name):
    return Path(__file__).parent / name


class AutohooksBlackTestCase(TestCase):
    def test_xblack_installed(self):
        sys.modules["black"] = None
        with self.assertRaises(Exception):
            check_black_installed()

    def test_get_black_arguments(self):
        args = get_black_arguments(config=None)
        self.assertEqual(args, DEFAULT_ARGUMENTS)

    def test_get_black_config(self):
        config_path = get_test_config_path("pyproject.test.toml")
        self.assertTrue(config_path.is_file())

        autohooksconfig = load_config_from_pyproject_toml(config_path)

        black_config = get_black_config(autohooksconfig.get_config())
        self.assertEqual(black_config.get_value("foo"), "bar")

    def test_ensure_iterable(self):
        foo = "bar"  # pylint: disable=blacklisted-name
        bar = ensure_iterable(foo)  # pylint: disable=blacklisted-name
        self.assertEqual(bar, ["bar"])

        foo = ["bar"]  # pylint: disable=blacklisted-name
        bar = ensure_iterable(foo)  # pylint: disable=blacklisted-name
        self.assertEqual(bar, ["bar"])

    def test_get_include_from_config(self):
        include = get_include_from_config(config=None)
        self.assertEqual(include, DEFAULT_INCLUDE)

    @patch("autohooks.plugins.black.black.ok")
    def test_precommit(self, _ok_mock):
        ret = precommit()
        self.assertFalse(ret)

    # these Terminal output functions don't run in the CI ...
    @patch("autohooks.plugins.black.black.ok")
    @patch("autohooks.plugins.black.black.error")
    @patch("autohooks.plugins.black.black.get_staged_status")
    def test_precommit_staged(self, staged_mock, _error_mock, _ok_mock):
        staged_mock.return_value = [StatusEntry("M  tests/black_test.py")]
        ret = precommit()
        self.assertFalse(ret)
