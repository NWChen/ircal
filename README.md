ircal
=====

[![Build Status](https://travis-ci.org/NWChen/ircal.svg?branch=master)](https://travis-ci.org/NWChen/ircal)

```ircal``` is an analytics dashboard for infrared radiometry data. It enables data visualization, calibration, and control of a system comprised of a blackbody radiation emitter and an infrared radiometer. 

---

## Installation

### From source

```bash
$ git clone https://github.com/NWChen/ircal.git
$ cd ircal
$ make
```

---

## App Structure

- ```docs``` contains project documentation generated automatically by pdoc from docstrings in source files. If you would like to regenerate documentation, then:
    ```bash
    $ cd ircal
    $ make docs
    ```
- ```src``` contains all source files, including KT/CT and blackbody drivers and dashboard code.
- ```test``` contains all unit tests for this project. If you make a change and would like to test it prior to deploying the application, then:
    ```bash
    $ cd ircal
    $ make test
    ```
