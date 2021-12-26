# -----------
# SPDX-License-Identifier: MIT
# Copyright (c) 2021 Troy Williams

# uuid       =
# author     = Troy Williams
# email      = troy.williams@bluebill.net
# date       =
# -----------

# -----------
# Information

# This is the prototype for the main Makefile in Python code repositories. It
# will make use of the `Makefile.python` to deal with the majority of python
# functionality that the repos will require. It will also help to make the main
# Makefile clean and contain only specific things that are required for the
# individual repository.

# -----------
# Default Target

# What happens when we just type `make`. This section will set it up so that the
# help strings are displayed.

# https://www.gnu.org/software/make/manual/html_node/How-Make-Works.html
# https://stackoverflow.com/questions/2057689/how-does-make-app-know-default-target-to-build-if-no-target-is-specified

# NOTE: We would have to override the .DEFAULT_GOAL in the main Makefile, after the include

.DEFAULT_GOAL := help

# -----------
# Makefile.env

# Makefile.env - should not be included with your repo. There is a
# Makefile.env.sample that exists with the variables that these makefiles
# require. Please make of copy of that, rename it and update the variables. Also
# add it to the .gitignore file.

include Makefile.env

# -----------
# Optional Includes

# Include the other makefile definitions you need for a specific project by
# copying them from the repo template repository and adding the proper includes
# here.

include Makefile.python
include Makefile.python.build
include Makefile.jupyter


# -----
# make clean

# Remove any created documents from the build process. This will probably be
# custom for every repo.

## make clean - Remove the build components
.PHONY: clean
clean:
	@echo "Cleaning PyPI build folder..."
	@rm -rf build
	@echo "Cleaning PyPI dist folder..."
	@rm -rf dist
	@echo "Cleaning Build Output..."
	@rm -rf output

# ------
# make remove

# Remove the Virtual Environment and clean the cached files.

# NOTE: For some repos, it might be prudent to add `clean` as a dependency.

## make remove - Remove the virtual environment and all cache files.
.PHONY: remove
remove: remove-venv
	@echo "Removing ${VENV} and Cached Files..."


# -----------
# make help

# - https://swcarpentry.github.io/make-novice/08-self-doc/index.html use sed to
#   look for double # pattern and use that as the documentation string to print
#   out.

# NOTE: This version uses find to find all makefiles and then feeds them to SED
# to extract the information.

## make help - List the available command descriptions for the Makefile.
.PHONY : help
help : $(wildcard Makefile)
	@echo ""
	@echo "Available Commands:"
	@echo ""
	@find . -name "Makefile*" -exec sed -n 's/^##//p' {} \;
	@echo ""
	@echo "To get started, use '$ make venv'"