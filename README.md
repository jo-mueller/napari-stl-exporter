# napari-stl-exporter

[![License](https://img.shields.io/pypi/l/napari-stl-exporter.svg?color=green)](https://github.com/jo-mueller/napari-stl-exporter/raw/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-stl-exporter.svg?color=green)](https://pypi.org/project/napari-stl-exporter)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-stl-exporter.svg?color=green)](https://python.org)
[![tests](https://github.com/jo-mueller/napari-stl-exporter/workflows/tests/badge.svg)](https://github.com/jo-mueller/napari-stl-exporter/actions)
[![codecov](https://codecov.io/gh/jo-mueller/napari-stl-exporter/branch/main/graph/badge.svg?token=9zctLzazD9)](https://codecov.io/gh/jo-mueller/napari-stl-exporter)

This plugin allows to import and export surface data in Napari to common file formats. The generated file formats can be read by other common applications, and - in particular - allow *3D-printing*.

<img src="https://github.com/jo-mueller/napari-stl-exporter/blob/main/doc/model_and_printed_model.png" width=80% height=80%>


### Supported file formats:
Currently supported file formats for export include and rely on the [vedo io API](https://vedo.embl.es/autodocs/content/vedo/io.html#vedo.io).
* *.stl*: [Standard triangle language](https://en.wikipedia.org/wiki/STL_%28file_format%29)
* *.ply*: [Polygon file format](https://en.wikipedia.org/wiki/PLY_(file_format))
* *.obj*: [Wavefront object](https://en.wikipedia.org/wiki/Wavefront_.obj_file)

### Supported Napari layers:

Currently supported Napari layer types are:
* [Surface layers](https://napari.org/howtos/layers/surface.html)
* [Label layers](https://napari.org/howtos/layers/labels.html): The label data is converted to surface data under the hood using the [marching cubes algorithm](https://scikit-image.org/docs/dev/api/skimage.measure.html#skimage.measure.marching_cubes) implemented in [scikit-image](https://scikit-image.org/) and is then exported using [Vedo](https://vedo.embl.es/). Warning: This can be slow for large image data!

### Import/export

**Interactively:** To export the data, simply save the selected layer with `File > Save Selected Layer(s)` and specify the file ending to be `some_file.[file_ending]`, for supported file types, see above. Similarly, supported file types can be imported into Napari with `File > `

**From code**: A [Napari Label layer](https://napari.org/api/napari.layers.Labels.html) can be added to the viewer as described in the [napari reference](https://napari.org/gallery/add_labels.html?highlight=add_labels) with this code snippet:

```python
import napari
import numpy as np

# Load and binarize image
label_image = np.zeros((100, 100, 100), dtype=int)
label_image[25:75, 25:75, 25:75] = 1

# Add data to viewer
viewer = napari.Viewer()
label_layer = viewer.add_labels(data, name='3D object')

# save the layer as 3D printable file to disc
napari.save_layers(r'/some/path/test.stl', [label_layer])
```

### Sample data
You can create sample label/surface data for export using the built-in functions as shown here:

<img src="https://github.com/jo-mueller/napari-stl-exporter/blob/main/doc/1_sample_data.png" width=45% height=45%>

...or from code with

```Python
import napari_stl_exporter

pyramid = napari_stl_exporter.make_pyramid_surface()

```

### 3D-printing
To actually send your object to a 3D-printer, it has to be further converted to the *.gcode* format with a Slicer program. The latter convert the 3D object to machine-relevant parameters (printing detail, motor trajectories, etc). Popular slicers are:

* [Slic3r](https://slic3r.org/): Documentation [here](https://manual.slic3r.org/intro/overview)
* [Prusa Slicer](https://www.prusa3d.com/prusaslicer/): Tutorial [here](https://help.prusa3d.com/en/article/first-print-with-prusaslicer_1753)

*Note*: You can also upload the STL file to [github.com](https://github.com) and interact with it in the browser:

<img src="https://github.com/jo-mueller/napari-stl-exporter/blob/main/doc/pyramid_browser_screenshot.png" width=45% height=45%>

** Digital elevation models**

DIgital elevation models (DEMs) can be printed with the st-exporter following these steps:

1. Go to the [open topography repository](https://portal.opentopography.org/raster?opentopoID=OTSDEM.032021.4326.2) and select a region of your choice, then download it as a GeoTiff file (`.tif`, intensity encodes elevation)
2. Open the downloaded tif image use the image conversion plugin (´Plugins > napari-stl-exporter > 2D image to surface´) to convert the downloaded image to a surface. CHeck the `solidify` option to make it readily 3D-printable.

<img src="https://github.com/jo-mueller/napari-stl-exporter/blob/main/doc/landscape_to_surface.png">

3. Export the created surface layer as `.stl` or `.ply` file. Open it in your Slicer of choice (you may have to scale it according to the size limitations of your printer) and off you go!

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using with [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/docs/plugins/index.html
-->

## Installation

You can install `napari-stl-exporter` via [pip]:

    pip install napari-stl-exporter

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-stl-exporter" is free and open source software

## Issues

If you encounter any problems, please [file an issue](https://github.com/jo-mueller/napari-stl-exporter/issues) along with a detailed description or post to image.sc and tag ```El_Pollo_Diablo```

[napari]: https://github.com/napari/napari
[Cookiecutter]: https://github.com/audreyr/cookiecutter
[@napari]: https://github.com/napari
[MIT]: http://opensource.org/licenses/MIT
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[GNU GPL v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[GNU LGPL v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[Apache Software License 2.0]: http://www.apache.org/licenses/LICENSE-2.0
[Mozilla Public License 2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
[cookiecutter-napari-plugin]: https://github.com/napari/cookiecutter-napari-plugin

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
