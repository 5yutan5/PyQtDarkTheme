Theme Color
===========

You can customize your theme color with the argument ``custom_colors`` of ``qdarktheme.load_stylesheet`` and ``qdarktheme.load_palette``.

.. code-block:: python

  import qdarktheme

  qdarktheme.load_stylesheet(custom_colors={"primary": "#D0BCFF"})
  # or
  qdarktheme.load_palette(custom_colors={"primary": "#D0BCFF"})

To customize a specific theme only, use the following syntax:

.. code-block:: python

  import qdarktheme

  qdarktheme.load_stylesheet(
      custom_colors={
          "[dark]": {
              "primary": "#D0BCFF",
          }
      }
  )

Color formats
-------------

+--------------------------------------+--------------------------------------+
| Format                               | Example                              |
+======================================+======================================+
| Case-insensitive hex RGB or RGBA     | - ``'#0f0f0f'``                      |
| string.                              | - ``'#0f0f0f80'``                    |
+--------------------------------------+--------------------------------------+
| Case-insensitive RGB or RGBA string  | - ``'#abc'`` as ``'#aabbcc'``        |
| equivalent hex shorthand of          | - ``'#fb1'`` as ``'#ffbb11'``        |
| duplicated characters.               | - ``'#e35f'`` as ``'#ee3355ff'``     |
+--------------------------------------+--------------------------------------+

List of customizable colors
---------------------------
