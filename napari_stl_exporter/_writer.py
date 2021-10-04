"""
This module is an example of a barebones writer plugin for napari

It implements the ``napari_get_writer`` and ``napari_write_image`` hook specifications.
see: https://napari.org/docs/dev/plugins/hook_specifications.html

Replace code below according to your needs
"""

from napari_plugin_engine import napari_hook_implementation

from skimage import measure
from stl import mesh


@napari_hook_implementation
def napari_get_writer(path: str):
    
    """Returns an stl Napari project writer if the path file format is stl.
    Parameters
    ----------
    path: str
        Napari stl project file
        
    Returns
    -------
    Callable or None
        Napari stl project file writer if the path file extension is correct
    """

    if isinstance(path, str) and path.endswith(".stl"):
        # If we recognize the format, we return the actual reader function
        return label_writer
    else:
        # otherwise we return None.
        return None

    

def label_writer(path: str, data: Any, meta: dict,
                 layer_type: str) -> str or None:
    
    """Write a 3D labels layer to stl

    Parameters
    ----------
    path : str 
        Path save to disk. Must end with .zarr
    data : array
        Labels data to be written
    meta : dict
        Labels metadata
    Returns
    -------
    str or None
        path if any labels were written, otherwise None
    """

    if isinstance(path, str) and path.endswith('.stl'):
    
        # binarize labels
        labels[labels != 0] = 1
    
        # marching cubes
        verts, faces, normals, values = measure.marching_cubes(labels, 0)
        
        # Create the mesh
        obj = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
        for i, f in enumerate(faces):
            for j in range(3):
                obj.vectors[i][j] = vertices[f[j],:]
                
        # Write the mesh to file
        obj.save(path)

        return path
    
    else:
        return None


