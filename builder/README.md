# Build resources

If you changed the contents in this folder, you need rebuild resources.

To build resources, run:

```Plaintext
poetry run python -m builder
```

Build svg and stylesheet based on the color-map of the theme file.
The resources are output to `qdarktheme/dist`.
This program is not included in the built package.

## Output format

```Plaintext
dist
├── __init__.py
├── dark
│   ├── __init__.py
│   ├── palette.py
│   ├── rc_icons.py
│   ├── stylesheet.py
│   └── svg
│       └── ...
└── light
    ├── __init__.py
    ├── palette.py
    ├── rc_icons.py
    ├── stylesheet.py
    └── svg
        └── ...
```
