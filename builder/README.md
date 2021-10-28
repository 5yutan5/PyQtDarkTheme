### Build resources

If you changed the contents in this folder, you need rebuild resources.

To build resources, run:

```Plaintext
poetry run python -m builder
```

Build svg and stylesheet based on the color-map of the theme file.
The resources are output to `qdarktheme/dist`.
This program is not included in the built package.

#### Output format

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

#### Use Json Schema for color map files

For VS Code, see https://code.visualstudio.com/docs/languages/json#_json-schemas-and-settings

To use the json schema, input following setting in `settings.json`.

```Json
"json.schemas": [
    {
        "fileMatch": [
            "/builder/theme/*"
        ],
        "url": "/builder/theme/validate.json"
    }
]
```
