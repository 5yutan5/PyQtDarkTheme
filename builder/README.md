Build svg and stylesheet based on the color-map of the theme file.
The resources are output to `qdarktheme/dist`.
To build resources, run:

```Plaintext
python -m builder
```

#### Output format

```Plaintext
dist
├── __init__.py
├── dark
│   ├── __init__.py
│   ├── stylesheet.qss
│   └── svg
│       └── ...
└── light
    ├── __init__.py
    ├── stylesheet.qss
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
