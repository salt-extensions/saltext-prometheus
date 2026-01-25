The changelog format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

This project uses [Semantic Versioning](https://semver.org/) - MAJOR.MINOR.PATCH

# Changelog

## 2.1.0 (2024-02-22)


### Fixed

- Fix `salt_aborted` metric lacking a state label [#26](https://github.com/salt-extensions/saltext-prometheus/issues/26)


## 2.0.3 (2023-08-14)

### Fixed

- Fix salt deps by removing them (#22)


## 2.0.2 (2023-03-13)

### Fixed

- Fix mode set to int octal instead of octal notation (#21)


## 2.0.1 (2023-03-12)

### Fixed

- Fix KeyError thrown when requiring state is not run (#20)


## 2.0.0 (2022-10-13)

### Added

- Add ability to use prometheus_client library (#2)


## 1.1.1 (2022-05-04)

### Added

- Hide raw version numbers to normalize data on release version (#6)


## 1.0.1 (2022-03-18)

### Fixed

- Fix textfile output to view None result as success (#3)


## 1.0.0 (2022-01-29)

### Added

- Initial version of Prometheus Text Exposition Format Returner
