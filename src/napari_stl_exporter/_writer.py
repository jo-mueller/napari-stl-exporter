import os
from skimage import measure
import vedo

from napari.types import LabelsData, SurfaceData
from typing import Optional


supported_layers = ['labels']
supported_formats = ['.stl', '.ply', '.obj']

def napari_write_surfaces(path: str, data: SurfaceData, meta: dict
                         ) -> Optional[str]:
    file_ext = os.path.splitext(path)[1]
    if file_ext in supported_formats:
        mesh = vedo.mesh.Mesh((data[0], data[1]))
        vedo.write(mesh, path)

        return path


def napari_write_labels(path: str, data: LabelsData, meta: dict
                        ) -> Optional[str]:

    file_ext = os.path.splitext(path)[1]
    if file_ext in supported_formats:

        mesh = _labels_to_mesh(data)
        vedo.write(mesh, path)

        return path

def _labels_to_mesh(label_image: LabelsData) -> vedo.mesh.Mesh:
    "Convert a label image to vedo mesh"
    # Binarize, retrieve surface and turn into vedo mesh
    label_image[label_image != 0] = 1
    verts, faces, normals, values = measure.marching_cubes(label_image, 0)
    mesh = vedo.mesh.Mesh((verts, faces))

    return mesh
