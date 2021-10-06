"""
This module is an example of a barebones writer plugin for napari

It implements the ``napari_get_writer`` and ``napari_write_image`` hook specifications.
see: https://napari.org/docs/dev/plugins/hook_specifications.html

Replace code below according to your needs
"""

import os
from skimage import measure
from stl import mesh
import numpy as np

from napari_plugin_engine import napari_hook_implementation

supported_layers = ['labels']

@napari_hook_implementation
def napari_get_writer(path, layer_types):
    
    # Check that only supported layers have been passed
    for lt in set(layer_types):
        if lt not in supported_layers:
            return None
    
    if isinstance(path, str) and path.endswith('.stl'):
        return napari_write_image
    else:
        return None


@napari_hook_implementation
def napari_write_labels(path, data, meta):
    
    if isinstance(path, str) and path.endswith('.stl'):
        data = np.asarray(data)
        data = 1
        # binarize labels
        data[data != 0] = 1
    
        # marching cubes
        verts, faces, normals, values = measure.marching_cubes(data, 0)
        
        # Create the mesh
        obj = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
        for i, f in enumerate(faces):
            for j in range(3):
                obj.vectors[i][j] = verts[f[j],:]
                
        # Write the mesh to file
        obj.save(path)
        print(f'stl written to {path}')
        return path
    
    else:
        return None
