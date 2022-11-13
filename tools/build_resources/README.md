# Build resources

If you changed the contents in this folder, you need to rebuild resources.
Resources rebuild automatically by pre-commit.

To build resources, run:

```Plaintext
poetry run python -m tools.build_resources
```

Build template stylesheet, svg, QPalette script and dark/light color values.
The resources are output to `./qdarktheme/_resources`.
This folder is not included in the built package.

## Output format

```Plaintext
resources
├── __init__.py
├── _color_values.py
├── _palette.py
├── _svg.py
└── _template_stylesheet.py
```
