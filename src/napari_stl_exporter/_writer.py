"""
This module is an example of a barebones writer plugin for napari

It implements the ``napari_get_writer`` and ``napari_write_image`` hook specifications.
see: https://napari.org/docs/dev/plugins/hook_specifications.html

Replace code below according to your needs
"""

import os
from skimage import measure

from napari_plugin_engine import napari_hook_implementation
from napari.types import LabelsData, SurfaceData
import vedo

supported_formats = ['.stl', '.ply']

@napari_hook_implementation
def napari_write_surface(path:str, data: SurfaceData, meta) -> str:

    file_ext = os.path.splitext(path)[1]
    if isinstance(path, str) and file_ext in supported_formats:

        mesh = vedo.mesh.Mesh((data[0], data[1]))
        vedo.write(mesh, path)

        return path
    
    else:
        return None

@napari_hook_implementation
def napari_write_labels(path:str, data: LabelsData, meta) -> str:

    file_ext = os.path.splitext(path)[1]
    if isinstance(path, str) and file_ext in supported_formats:

        mesh = _labels_to_mesh(data)
        vedo.write(mesh, path)

        return path
    
    else:
        return None

def _labels_to_mesh(label_image: LabelsData) -> vedo.mesh.Mesh:
    "Convert a label image to vedo mesh"
    # Binarize, retrieve surface and turn into vedo mesh
    label_image[label_image != 0] = 1
    verts, faces, normals, values = measure.marching_cubes(label_image, 0)
    mesh = vedo.mesh.Mesh((verts, faces))

    return mesh
