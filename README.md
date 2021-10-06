# napari-stl-exporter

[![License](https://img.shields.io/pypi/l/napari-stl-exporter.svg?color=green)](https://github.com/jo-mueller/napari-stl-exporter/raw/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-stl-exporter.svg?color=green)](https://pypi.org/project/napari-stl-exporter)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-stl-exporter.svg?color=green)](https://python.org)
[![tests](https://github.com/jo-mueller/napari-stl-exporter/workflows/tests/badge.svg)](https://github.com/jo-mueller/napari-stl-exporter/actions)
[![codecov](https://codecov.io/gh/jo-mueller/napari-stl-exporter/branch/master/graph/badge.svg)](https://codecov.io/gh/jo-mueller/napari-stl-exporter)

Exports label images to 3D-printable stl files. 

## Features

Starting point is a label layer, e.g. after image segmentation. See this [list for napari's segmentation plugins](https://www.napari-hub.org/?search=segmentation&sort=relevance&page=1).
![](https://raw.githubusercontent.com/jo-mueller/napari-stl-exporter/main/doc/head_screenshot.png)

Alternatively, you can load a binary image, e.g. as TIF image and then easily create label layers from an image layer in napari right-clicking on the layer and by converting the layer:
![](https://raw.githubusercontent.com/jo-mueller/napari-stl-exporter/main/doc/convert_to_label.png)

The label layer is then saved as a 3D-printable stl file if the filename is provided accordingly (e.g., _MyExampleFile.stl_). To actually send your object to a 3D-printer, it has to be further converted with a Slicer program which actually controls the print parameters (Level of detail, layer thickness, etc). Popular freeware slicers are:

* [Slic3r](https://slic3r.org/)
* [Prusa Slicer](https://www.prusa3d.com/prusaslicer/)

You can also upload the STL file to [github.com](https://github.com) and interact with it in the browser:
![](https://raw.githubusercontent.com/jo-mueller/napari-stl-exporter/main/doc/head_screenshot_browser.png)

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
