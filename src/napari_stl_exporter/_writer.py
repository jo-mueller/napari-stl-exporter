import os
from skimage import measure
import vedo

from napari.types import LabelsData, SurfaceData, PointsData
from typing import Optional


supported_layers = ['labels']
supported_surface_formats = ['.stl', '.ply', '.obj']
supported_points_formats = ['.vtp']


def napari_write_surfaces(path: str, data: SurfaceData, meta: dict
                         ) -> Optional[str]:
    file_ext = os.path.splitext(path)[1]
    if file_ext in supported_surface_formats:
        mesh = vedo.mesh.Mesh((data[0], data[1]))
        vedo.write(mesh, path)

        return path


def napari_write_points(
        path: str, data: PointsData, meta: dict
        ) -> Optional[str]:
    file_ext = os.path.splitext(path)[1]
    if file_ext in supported_points_formats:
        points = vedo.Points(data)

        # if metadata doesn't exist
        if meta is None:
            vedo.write(points, path)
            return path

        # add features to pointcloud
        if 'properties' in meta:
            features = meta['properties']
        elif 'features' in meta:
            features = meta['features']
        for key in features:
            points.pointdata[key] = features[key]
        vedo.write(points, path)

        return path


def napari_write_labels(path: str, data: LabelsData, meta: dict
                        ) -> Optional[str]:

    file_ext = os.path.splitext(path)[1]
    if file_ext in supported_surface_formats:

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
