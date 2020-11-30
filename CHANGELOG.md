# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
* Adding pontos module for future releases [#60](https://github.com/greenbone/autohooks-plugin-black/pull/60)
* Adding tests for this plugin [#89](https://github.com/greenbone/autohooks-plugin-black/pull/89)

### Changed
Replaced pipenv with poetry for dependency management. poetry install works a bit different than pipenv install. It installs dev packages. [#51](https://github.com/greenbone/autohooks-plugin-black/pull/51)

### Fixed
### Removed

[Unreleased]: https://github.com/greenbone/autohooks-plugin-black/compare/v1.2.0...master

## [1.2.0] - 2019-11-21

### Added
* Allow to configure the arguments for black in *pyproject.toml* [#19](https://github.com/greenbone/autohooks-plugin-black/pull/19)

[1.2.0]: https://github.com/greenbone/autohooks-plugin-black/compare/v1.1.0...v1.2.0

## [1.1.0] - 2019-03-28

### Changed

* Changed git repository location to https://github.com/greenbone/autohooks-plugin-black
* Allow to configure files to be formatted [#1](https://github.com/greenbone/autohooks-plugin-black/pull/1)
* Use new autohooks status API to print messages [#2](https://github.com/greenbone/autohooks-plugin-black/pull/2)

[1.1.0]: https://github.com/greenbone/autohooks-plugin-black/compare/v1.0.0...v1.1.0
