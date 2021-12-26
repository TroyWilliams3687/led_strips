# Python Repository Template

## Introduction

This is a set of Makefiles that are used as a starting point to provide common features for python repositories. The goal is to make using a python based repo, cross-platform as simple as possible. Normally constructing the virtual environment can be a chore. This set of makefiles simplifies that process considerable.

Simply copy the makefiles to your repository root and issue the terminal command (at the repo root):

```bash
$ make venv
```

That command will construct the virtual environment based on the particular python version you want. It will look for all `requirements.txt` files and install all modules automatically. If your python project is a package itself, it will automatically install it in the virtual environment.

To delete the virtual environment issue `make remove` and that will remove the `.venv` along with all python cache folders and other items that are not required.

## Usage

There are quite a few files in this repository. All of them can be used as a basis of a new Python project repository. Or you can cherry-pick the ones that are relevant.


### Basics - Repo and Package


- `.gitignore`
    - basic boilerplate for `.gitignore` cobbled together from other sources with some things removed. A good starting point.

- `dev-requirements.txt`
    - The requirements file template for development dependencies. The makefiles are setup to read any `*requirements.txt` at the root of the repo. This gives you the ability to organize the dependencies any way you see fit. The basics in this repo divides items your project needs (i.e. `requirements.txt`) from development dependencies like linters.
    - NOTE: This isn't required if you are not creating a package where the required modules can be different.

- `requirements.txt`
    - Same as the `dev-requirements.txt`, just for things your project/package needs.

- `pyproject.toml`
    - a basic template TOML file used in the package build process. This is only required if you project is a package or will be treated like a package. It is boilerplate and doesn't require any changes or modifications.
    - NOTE: This isn't required if you are not creating a package.

- `setup.py`
    - The `setup.py` is modified to work with `pyproject.toml`. As such, it is a boilerplate file that only requires to be in the root folder. Nothing in this file needs to be modified.
    - NOTE: This isn't required if you are not creating a package.

- `setup.cfg`
    - The new way to build python packages. The `setup.cfg` is an excellent template and can easily be adapted to various projects.
    - NOTE: This isn't required if you are not creating a package.


>NOTE: For a basic project, only the `.gitignore` and `requirements.txt` files should be used.

### Make

The makefiles are the reason for this repository. They provide functionality in a common way across different python repositories. It makes that using a command like `make venv` will construct the virtual environment and install all the requirements. It means that `make test` will run pytest (if installed). 

For the makefiles to work properly, we have to define the `Makefile.env`. This file should not be stored in the repository, add it to `.gitignore` (if you use the template in this repo, it is already there). `Makefile.env` stores the path to the Python binaries that you want to use. This means it is possible to use different versions of Python if you want in a way that is transparent and flexible (at least I think so). There are two sample files, one for Linux (bash) and one for windows. Rename the appropriate one and set the path correctly.

- `Makefile.env`
- `Makefile.env.sample`
- `Makefile.env.win.sample`

Once the `Makefile.env` is properly configured it is time to add the rest of the makefiles. For a basic Python repository, you should use the following 3 makefiles:

- `Makefile`
    - This is the root makefile. It defines a lot of the commands and it includes (imports) the other more specialized makefiles.

- `Makefile.python`
    - This is Python specific commands around constructing and managing the virtual environments. 
    - It is simply included into the main makefile.

- `Makefile.python.build`
    - This Python specific commands around testing and linting.
    - It is simply included into the main makefile.

Optionally, you can include these makefiles to provide more specialized support. You can also create your own.

- `Makefile.docker`
- `Makefile.jupyter`

## Basic Commands


Help:

```bash
$ make
```

Delete `.venv` and other python folders (caches and temp folders):

```bash
$ make remove
```

Build virtual environment (`.venv`): 

```bash
$ make venv
```

Launch virtual environment: 

```bash
$ make shell
```

Run unit tests:

```bash
$ make test
```


## License

[MIT](https://choosealicense.com/licenses/mit/)

