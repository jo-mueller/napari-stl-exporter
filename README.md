# napari-stl-exporter

[![License](https://img.shields.io/pypi/l/napari-stl-exporter.svg?color=green)](https://github.com/jo-mueller/napari-stl-exporter/raw/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-stl-exporter.svg?color=green)](https://pypi.org/project/napari-stl-exporter)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-stl-exporter.svg?color=green)](https://python.org)
[![tests](https://github.com/jo-mueller/napari-stl-exporter/workflows/tests/badge.svg)](https://github.com/jo-mueller/napari-stl-exporter/actions)
[![codecov](https://codecov.io/gh/jo-mueller/napari-stl-exporter/branch/master/graph/badge.svg)](https://codecov.io/gh/jo-mueller/napari-stl-exporter)

This plugin allows to convert 3D label images to 3D-printable [*.stl*, *.ply*] files using the [marching cubes algorithm](https://scikit-image.org/docs/dev/api/skimage.measure.html#skimage.measure.marching_cubes) implemented in [scikit-image](https://scikit-image.org/). The generated files can then be read by common 3D-printing slicer programs (see below).

![input_output](https://user-images.githubusercontent.com/38459088/139666759-7b88bd80-313e-447c-9d9f-7489f810b753.png)

## Usage
The napari-stl-exporter requires labeled, 3D input data. To segment your 3D image and create 3D label images out of it, see this [list of napari's image segmentation plugins](https://www.napari-hub.org/?search=segmentation&sort=relevance&page=1).
The 3D label image can then be converted to a 3D-printable file by specifying the file extension to be one of the listed supported formats uppon image export in napari using the menu `File > Save selected layer(s)...`. 

**Supported formats:**
* *.stl*
* *.ply*

### Preparing label data
- **Interactively**: After loading a binary image ([example data](https://github.com/jo-mueller/napari-stl-exporter/tree/main/data)), e.g. by drag and drop the file onto the napari viewer, it might be neccessary to convert it to a labels layer using the right-click menu on the layer in the layer list and selecting ```Convert to Labels```: 

![](https://raw.githubusercontent.com/jo-mueller/napari-stl-exporter/main/doc/convert_to_label.png)

- **Programmatically**: A [Napari Label layer](https://napari.org/api/stable/napari.layers.Labels.html) can be added to the viewer as described in the [napari reference](https://napari.org/api/stable/napari.view_layers.Viewer.html?highlight=add_labels#napari.view_layers.Viewer.add_labels) with this code snippet:
```python
import napari
from skimage import io

# Load and binarize image
data = io.imread('/Path/to/input/data')
data[data != 0] = 1

# Add data to viewer
viewer = napari.Viewer()
label_layer = viewer.add_labels(data, name='3D object')

# save the layer as 3D printable file to disc
napari.save_layers(r'/some/path/test.stl', [label_layer])
```

### 3D-printing
To actually send your object to a 3D-printer, it has to be further converted to the *.gcode* format with a Slicer program. The latter convert the 3D object to machine-relevant parameters (printing detail, motor trajectories, etc). Popular slicers are:

* [Slic3r](https://slic3r.org/): Documentation [here](https://manual.slic3r.org/intro/overview)
* [Prusa Slicer](https://www.prusa3d.com/prusaslicer/): Tutorial [here](https://help.prusa3d.com/en/article/first-print-with-prusaslicer_1753)

You can also upload the STL file to [github.com](https://github.com) and interact with it in the browser:
![](https://raw.githubusercontent.com/jo-mueller/napari-stl-exporter/main/doc/pyramid_browser_screenshot.png)

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

If you encounter any problems, please [file an issue] along with a detailed description or post to image.sc and tag ```El_Pollo_Diablo```

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
