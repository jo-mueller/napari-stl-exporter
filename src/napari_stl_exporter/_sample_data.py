from __future__ import annotations
from skimage import io, measure
import pathlib, os
from napari.types import LayerDataTuple

# Taken from https://github.com/zoccoler/napari-metroid/blob/main/src/napari_metroid/_sample_data.py

parent = pathlib.Path(__file__).parent.resolve()
fname = os.path.join(parent, 'sample_data', 'Pyramid.tif')

def make_pyramid_label() -> LayerDataTuple:
    """Generates a label image of a pyramid"""

    return [(io.imread(fname_pyramid), {}, 'labels')]

def make_pyramid_surface() -> LayerDataTuple:
    """Generates a surface layer of a pyramid"""
    Pyramid = io.imread(fname_pyramid)
    Pyramid = measure.marching_cubes(Pyramid)

    return [((Pyramid[0], Pyramid[1]), {}, 'surface')]

def make_landscape() -> LayerDataTuple:
    """Generate an imafge of a digital elevation model"""
    return [(io.imread(fname_saxony), {}, 'image')]
