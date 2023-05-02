# Build style resources

This tool build template stylesheet, svg, QPalette script and dark/light color values.
The resources are output to `{projectRootFolder}/qdarktheme/_resources`.

## Output format

``` shell
resources
├── __init__.py
├── _color_values.py
├── _palette.py
├── _svg.py
└── _template_stylesheet.py
```

Original data is in `{projectRootFolder}/style`. For more information about styles, see the `{projectRootFolder}/style/README.md`.
