"""Document configuration."""
# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

import os
import sys
import time
from datetime import datetime
from importlib.metadata import metadata as package_metadata

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
sys.path.insert(0, os.path.abspath("../.."))


# -- Project information -----------------------------------------------------
project = "PyQtDarkTheme"
copyright = f"2021-2022, {package_metadata(project)['author']}"
author = package_metadata(project)["author"]

now = datetime.utcfromtimestamp(int(os.environ.get("SOURCE_DATE_EPOCH", time.time())))

version = package_metadata(project)["version"]
release = version

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.viewcode",
    "sphinx.ext.todo",
    "sphinx.ext.napoleon",
    "sphinx_panels",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_build", "Thumbs.db", ".DS_Store"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_css_files = [
    "installation_guide.css",
    "pyqtdarktheme.css",
]

html_theme_options = {
    "github_url": package_metadata(project)["home-page"],
}
