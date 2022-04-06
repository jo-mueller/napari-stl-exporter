import os
from skimage import measure
import vedo

from napari.types import LabelsData
from typing import Any, Optional


supported_layers = ['labels']
supported_formats = ['.stl', '.ply']

def napari_write_labels(path: str, data: Any, meta: dict) -> Optional[str]:

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
