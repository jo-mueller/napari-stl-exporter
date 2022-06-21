# -*- coding: utf-8 -*-
from napari.types import SurfaceData
import os
import vedo
import numpy as np

supported_formats = ['.stl', '.ply']

def napari_import_surface(path: str) -> SurfaceData:
    """
    Read supported surface files using the vedo io functionality.

    Parameters
    ----------
    path : str

    Returns
    -------
    SurfaceData

    """
    file_ext = os.path.splitext(path)[1]
    if file_ext in supported_formats:

        mesh = vedo.io.load(path, unpack=True, force=False)
        mesh = (mesh.points(), np.asarray(mesh.faces()))

        return mesh
