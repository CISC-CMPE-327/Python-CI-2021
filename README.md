# qBay - Python-CI-2021 template

[![Pytest-All](https://github.com/CISC-CMPE-327/Python-CI-2021/actions/workflows/pytest.yml/badge.svg)](https://github.com/CISC-CMPE-327/Python-CI-2021/actions/workflows/pytest.yml)
[![Python PEP8](https://github.com/CISC-CMPE-327/Python-CI-2021/actions/workflows/style_check.yml/badge.svg)](https://github.com/CISC-CMPE-327/Python-CI-2021/actions/workflows/style_check.yml)

This folder contains the template for A2 (backend dev). Folder structure:

```
├── LICENSE
├── README.md
├── .github
│   └── workflows
│       ├── pytest.yml       ======> CI settings for running test automatically (trigger test for commits/pull-requests)
│       └── style_check.yml  ======> CI settings for checking PEP8 automatically (trigger test for commits/pull-requests)
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

For the ORM API of flask+sqlalchemy, more exampales can be found here:
https://flask-sqlalchemy.palletsprojects.com/en/latest/queries/#insert-update-delete

##  GitHub Actions (for Continuous Integration): :ok_hand:
With GitHub Actions, you will be able to automatically run all your test cases directly on the cloud, whenever you make changes to your codebase. GitHub actions are available by default. You will be able to use GitHub Actions for your course project. You will have 2,000 minutes test runtime per month for your project. You will find that at your repository homepage there is a tab ‘Actions’. You will be able to find all the logs of all the test runs, and where it broke (using this repo as an example): 

<p align="center">
  <img width="800"  src="https://user-images.githubusercontent.com/8474647/135193096-0f2068b9-e3cb-4197-ae8d-91c58f97aba8.png">
</p>

Setting up GitHub Actions workflow for your project is simple. Workflows are defined in yml files. The xxx.yml file in the folder `.github/workflows` define the workflow of your CI process. 

<p align="center">
  <img width="400"  src="https://user-images.githubusercontent.com/8474647/135193263-1bbf3e17-7d5e-4e2a-b864-3577ee00c5ac.png">
</p>

As an example, this is a yml file we use here to automatically check the code's style compliance to PEP8.

- `name`: the name of your CI process. Can be anything. You name it.
- `on`: the event for which will trigger your CI process. Here we add push. Means that everytime you push your code to the repository, it will trigger the script to run!
- `runs-on`: which platform you would like the test case to run on.
- `steps`: steps to carry out in sequence.
- `uses`: leverage existing operations defined in github actions. In this example, `actions/checkout@v1` means downloading the code.
- `name`: give a name to a step. Usually under the name item you will find a `run` item.
- `run`: the script/command to execute. (in this case, flake8)

These templates provide you a starting point to setup your repository and understand how the workflow works for GitHub Actions (well the other CI platforms all follow a similar idea, under the hood GitHub Actions uses M:heavy_dollar_sign: Azure pipelines). 

The `passing` badge on the homepage (in the README file) still points to the original template. So make sure that you update the link accordingly pointing to your repository.  You can find the link at the Action tab, click on one of the workflow, on the upper right corner, there is a `...` button that shows a `create status badge` menu where it will give you the full markdown link.

![image](https://user-images.githubusercontent.com/8474647/135193609-eb84b6f7-e825-4555-b096-69c353d4d71b.png)



