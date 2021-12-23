Contributing Guide
==================

All contributions, bug reports, bug fixes, documentation improvements, enhancements, and ideas are welcome.

Local development
-----------------

These are the basic steps needed to start developing on PyQtDarkTheme.

#. Clone PyQtDarkTheme
    You will first need to clone the repository using git and place yourself in its directory:

    .. code-block:: bash

        $ git@github.com:5yutan5/PyQtDarkTheme.git
        $ cd PyQtDarkTheme
#. Install Poetry
    You will need Poetry to start contributing on the PyQtDarkTheme codebase. Refer to the `Poetry documentation <https://python-poetry.org/docs/#installation>`__ to start using Poetry.
#. Create a virtual environment
    Now, you will need to install the required dependency for PyQtDarkTheme with Poetry and install Qt bindings(PySide or PyQt) with pip.

    .. code-block:: bash

        $ poetry install
        $ poetry run pip install PySide6

#. Run Pytest
    You need to be sure that the current tests are passing on your machine:

    .. code-block:: bash

        $ poetry run pytest tests
#. Setup pre-commit
    To make sure that you don't accidentally commit code that does not follow the coding style, you can install a pre-commit hook that will check that everything is in order:

    .. code-block:: bash

        $ poetry run pre-commit install
#. Check Qt theme
    You can check dark/light theme with example app.

    .. code-block:: bash

        $ poetry run python -m qdarktheme.widget_gallery
