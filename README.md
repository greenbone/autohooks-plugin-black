![Greenbone Logo](https://www.greenbone.net/wp-content/uploads/gb_logo_resilience_horizontal.png)

# autohooks-plugin-black

[![PyPI release](https://img.shields.io/pypi/v/autohooks-plugin-black.svg)](https://pypi.org/project/autohooks-plugin-black/)

An [autohooks](https://github.com/bjoernricks/autohooks) plugin for python code
formatting via [black](https://github.com/ambv/black).

## Installation

### Install using pip

You can install the latest stable release of autohooks-plugin-black from the
Python Package Index using [pip](https://pip.pypa.io/):

    pip install autohooks-plugin-black

Note the `pip` refers to the Python 3 package manager. In environment where
Python 2 is also available the correct command may be `pip3`.

### Install using pipenv

It is highly encouraged to use [pipenv](https://github.com/pypa/pipenv) for
maintaining your project's dependencies. Normally autohooks-plugin-black is
installed as a development dependency.

    pipenv install --dev autohooks-plugin-black

## Usage

To activate the black autohooks plugin please add the following setting to your
*pyproject.toml* file.

```toml
[tool.autohooks]
pre-commit = ["autohooks.plugins.black"]
```

## Maintainer

This project is maintained by [Greenbone Networks GmbH](https://www.greenbone.net/).

## Contributing

Your contributions are highly appreciated. Please
[create a pull request](https://github.com/bjoernricks/autohooks-plugin-black/pulls)
on GitHub. Bigger changes need to be discussed with the development team via the
[issues section at GitHub](https://github.com/bjoernricks/autohooks-plugin-black/issues)
first.

## License

Copyright (C) 2019 [Greenbone Networks GmbH](https://www.greenbone.net/)

Licensed under the [GNU General Public License v3.0 or later](LICENSE).
