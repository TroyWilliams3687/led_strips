# LED Strip Calculations

## Introduction

This is a set of Jupyter notebooks for use in LED projects for conical spirals. It helps to estimate the length required given the cone base radius, r, and its height, h. It also provides some electrical calculation templates. Each notebook should be self contained and descriptive enough.

## Installation and Usage

- Clone the repo 
- Create a `Makefile.env` at the root (`$ touch Makefile.env`)
    - Or you can copy the `Makefile.env.sample`  or `Makefile.env.win.sample` depending on your environment

Issue the following terminal command (at the repo root):

```bash
$ make launch
```

That command will construct the virtual environment based on the particular python version you want to use. It will look for all `requirements.txt` files and install all modules automatically. It will launch the Jupyter environment.

To delete the virtual environment issue `make remove` and that will remove the `.venv` along with all python cache folders and other items that are not required. This is a good way to get the latest versions of the packages.



### Make

The makefiles are the reason for this repository. They provide functionality in a common way across different python repositories. It makes that using a command like `make venv` will construct the virtual environment and install all the requirements. It means that `make test` will run pytest (if installed). 

For the makefiles to work properly, we have to define the `Makefile.env`. This file should not be stored in the repository. `Makefile.env` stores the path to the Python binaries that you want to use. This means it is possible to use different versions of Python if you want in a way that is transparent and flexible (at least I think so). There are two sample files, one for Linux (bash) and one for windows. Rename the appropriate one and set the path correctly.

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


- `Makefile.jupyter`
    - This is additional commands to launch the Jupyter environment.

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
$ make launch
```



## License

[MIT](https://choosealicense.com/licenses/mit/)

