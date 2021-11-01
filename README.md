# napari-stl-exporter

[![License](https://img.shields.io/pypi/l/napari-stl-exporter.svg?color=green)](https://github.com/jo-mueller/napari-stl-exporter/raw/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-stl-exporter.svg?color=green)](https://pypi.org/project/napari-stl-exporter)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-stl-exporter.svg?color=green)](https://python.org)
[![tests](https://github.com/jo-mueller/napari-stl-exporter/workflows/tests/badge.svg)](https://github.com/jo-mueller/napari-stl-exporter/actions)
[![codecov](https://codecov.io/gh/jo-mueller/napari-stl-exporter/branch/master/graph/badge.svg)](https://codecov.io/gh/jo-mueller/napari-stl-exporter)

This plugin allows to convert 3D label images to 3D-printable *.stl* files using the [marching cubes algorithm](https://scikit-image.org/docs/dev/api/skimage.measure.html#skimage.measure.marching_cubes) implemented in [scikit-image](https://scikit-image.org/). The generated stl-files can be [viewed on github](https://github.com/jo-mueller/napari-stl-exporter/blob/improve_documentation/doc/Pyramid.stl) and are readable for common 3D-printing slicer programs (see [below](https://github.com/jo-mueller/napari-stl-exporter/blob/improve_documentation/README.md#3d-printing)).

![input_output](https://github.com/jo-mueller/napari-stl-exporter/blob/improve_documentation/doc/input_output.png)

## Usage
Starting point is a label layer, e.g. after image segmentation. See this [list for napari's segmentation plugins](https://www.napari-hub.org/?search=segmentation&sort=relevance&page=1). The data is then converted to the 3D-printable *.stl* format simply by specifying the stl-file extension uppon image export in napari. For simple example data, see [here](https://github.com/jo-mueller/napari-stl-exporter/tree/main/data).


### Preparing label data
You can load a binary image, e.g. as TIF image and then easily create label layers from an image layer in napari right-clicking on the layer and by converting the layer:

- **Programmatically**: Download the [example data](https://github.com/jo-mueller/napari-stl-exporter/tree/improve_documentation/data) and add a [Napari Label layer](https://napari.org/api/stable/napari.layers.Labels.html) as described in the [napari reference](https://napari.org/api/stable/napari.view_layers.Viewer.html?highlight=add_labels#napari.view_layers.Viewer.add_labels) with this code snippet:
```python
import napari
from skimage import io

# Load and binarize image
data = io.imread('SomePath\Pyramid.tif')
data[data != 0] = 1

# Add data to viewer
viewer = napari.Viewer()
label_layer = viewer.add_labels(data, name='3D object')

```

- **Interactively**: Download the [example data](https://github.com/jo-mueller/napari-stl-exporter/tree/improve_documentation/data) data and open it with Napari. Convert it to a labels layer by rightclicking on the entry in the layer list and select ```Convert to Labels```: 

![](https://raw.githubusercontent.com/jo-mueller/napari-stl-exporter/main/doc/convert_to_label.png)

### Saving data
To save the model as an *.stl* file, export it by selecting ```File->Save Selected Layer(s)``` and save it as ```MyModel.stl```, which will automatically call the conversion. Alternativaley, use 

```napari.save_layers(r'SomePath\Pyramid.stl', [label_layer])```

to save the previously generated label layer as .stl file. The label layer is then saved as a 3D-printable *.stl* file if the filename is provided accordingly (e.g., ```Pyramid.stl```). 

### 3D-printing
To actually send your object to a 3D-printer, it has to be further converted to the *.gcode* format with a Slicer program. The latter convert the 3D object to machine-relevant parameters (printing detail, motor trajectories, etc). Popular slicers are:

* [Slic3r](https://slic3r.org/): Documentation [here](https://manual.slic3r.org/intro/overview)
* [Prusa Slicer](https://www.prusa3d.com/prusaslicer/): Tutorial [here](https://help.prusa3d.com/en/article/first-print-with-prusaslicer_1753)

## Known issues

- Missing walls in stl-model: In order for all object boundaries to be recognized correctly, it is necessary to have a layer of empty (i.e., zero-valued) voxels between the object and the image boundaries. Otherwise, some edges of the object may not be detected correctly.
- Large images: Processing large images (~ 1000 x 1000 x 100) requires large amount of memory. In this case it is advised to crop or resize (e.g., downsample) the input image.

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
