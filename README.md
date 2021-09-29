# qBay - Python-CI-2021 template

[![Pytest-All](https://github.com/CISC-CMPE-327/Python-CI-2021/actions/workflows/pytest.yml/badge.svg)](https://github.com/CISC-CMPE-327/Python-CI-2021/actions/workflows/pytest.yml)
[![Python PEP8](https://github.com/CISC-CMPE-327/Python-CI-2021/actions/workflows/style_check.yml/badge.svg)](https://github.com/CISC-CMPE-327/Python-CI-2021/actions/workflows/style_check.yml)

This folder contains the template for A2 (backend dev). Folder structure:

```
├── LICENSE
├── README.md
├── qbay                 ======> Application source code
│   ├── __init__.py      ======> Required for a python module (can be empty)
│   ├── __main__.py      ======> Program entry point
│   └── models.py        ======> Data models
├── qbay_test            ======> Testing code
│   ├── __init__.py      ======> Required for a python module (can be empty)
│   ├── conftest.py      ======> Code to run before/after all the testing
│   └── test_models.py   ======> Testing code for models.py
└── requirements.txt     ======> Dependencies
```

To run the application module (make sure you have a python environment of 3.5+)

```
$ pip install -r requirements.txt
$ python -m qbay
```

Currently it shows nothing since it is empty in the `__main__.py` file.
Database and the tables will be automatically created into a `db.sqlite` file if non-existed.

To run testing:

```
# style check (only show errors)
flake8 --select=E .  

# run all testing code 
pytest -s qbay_test

```
