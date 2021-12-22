# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Changed
* Update dependencies to latest releases [#209](https://github.com/greenbone/autohooks-plugin-black/pull/209)

[Unreleased]: https://github.com/greenbone/autohooks-plugin-black/compare/v21.7.1...HEAD


## [21.7.1] - 2021-07-26
### Changed
* Allow black up tp current 21.7b0 [#143](https://github.com/greenbone/autohooks-plugin-black/pull/143)

[21.7.1]: https://github.com/greenbone/autohooks-plugin-black/compare/v21.7.0...v21.7.1

## [21.7.0] - 2021-07-05
### Changed
* Don't depend on a single version of black and allow black versions up to current 21.6b0 [#131](https://github.com/greenbone/autohooks-plugin-black/pull/131)

[21.7.0]: https://github.com/greenbone/autohooks-plugin-black/compare/v21.6.0...v21.7.0

## [21.6.0] - 2021-06-13

### Added
* Adding pontos module for future releases [#60](https://github.com/greenbone/autohooks-plugin-black/pull/60)
* Adding tests for this plugin [#89](https://github.com/greenbone/autohooks-plugin-black/pull/89)

### Changed
Replaced pipenv with poetry for dependency management. poetry install works a bit different than pipenv install. It installs dev packages. [#51](https://github.com/greenbone/autohooks-plugin-black/pull/51)

[21.6.0]: https://github.com/greenbone/autohooks-plugin-black/compare/v1.2.0...v21.6.0

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
