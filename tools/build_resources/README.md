# Build resources

If you changed the contents in this folder, you need to rebuild resources.
Resources rebuild automatically by pre-commit.

To build resources, run:

```Plaintext
poetry run python -m tools.build_resources
```

Build svg and stylesheet based on the color-map of the theme file.
The resources are output to `./qdarktheme/themes`.
This folder is not included in the built package.

## Output format

```Plaintext
themes
├── __init__.py
├── dark
│   ├── __init__.py
│   ├── palette.py
│   ├── stylesheet.py
│   └── svg.py
└── light
    ├── __init__.py
    ├── palette.py
    ├── stylesheet.py
    └── svg.py
```
