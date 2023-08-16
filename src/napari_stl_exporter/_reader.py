# -*- coding: utf-8 -*-
from napari.types import LayerDataTuple
import os
import vedo
import numpy as np
from typing import Optional, List

supported_surface_formats = ['.stl', '.ply', '.obj']
suported_points_formats = ['.vtp']


def get_reader(path: str) -> Optional[callable]:
    # Taken from https://napari.org/plugins/guides.html

    file_ext = os.path.splitext(path)[1]
    if isinstance(path, str) and file_ext in supported_surface_formats:
        return napari_import_surface
    elif isinstance(path, str) and file_ext in suported_points_formats:
        return napari_import_points

    # otherwise we return None.
    return None


def napari_import_surface(path: str) -> List[LayerDataTuple]:
    """
    Read supported surface files using the vedo io functionality.

    Parameters
    ----------
    path : str

    Returns
    -------
    SurfaceData

    """
    mesh = vedo.load(path, unpack=True, force=False)
    _mesh = [mesh.points(), np.asarray(mesh.faces())]
    return [tuple([_mesh, {}, 'surface'])]


def napari_import_points(path: str) -> List[LayerDataTuple]:
    """
    Read supported point cloud files using the vedo io functionality.

    Parameters
    ----------
    path : str

    Returns
    -------
    PointsData

    """
    import pandas as pd
    points = vedo.load(path, unpack=True, force=False)
    features = pd.DataFrame(dict(points.pointdata))
    return [(points.points(), {'features': features,
                               'face_color': features.columns[0]}, 'points')]
