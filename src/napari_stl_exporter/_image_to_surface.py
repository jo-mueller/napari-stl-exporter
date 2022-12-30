from napari.types import ImageData, SurfaceData
from itertools import product
from magicgui import magic_factory

@magic_factory
def extrude(surface: SurfaceData, distance: float = 1.0) -> SurfaceData:
    """
    Extrude a mesh by a given value.

    This offsets all vertices in a mesh by a given value. New faces will be created
    at the edge of non-closed meshs, thus solidifying meshes.
    
    Parameters
    ----------
    surface: SUrfaceData

    Returns
    -------
    surface: SurfaceData
    """
    import vedo
    import numpy as np

    mesh = vedo.mesh.Mesh((np.flip(surface[0], axis=1), surface[1]))
    mesh = mesh.extrude(zshift=distance)

    return (np.flip(mesh.points(), axis=1), np.asarray(mesh.faces()))

@magic_factory
def image_to_surface(image: ImageData, z_multiplier: float = 1.0) -> SurfaceData:
    """
    Convert a 2D image to a surface mesh. The image intensity is used as z-coordinate of the mesh.

    Parameters
    ----------
    image : ImageData

    z_multiplier: Multiplies the intensity-derived z-coordinate with this factor.
    
    Returns
    -------

    surface: SUrfaceData
    """

    import numpy as np
    from scipy import spatial

    x = np.arange(image.shape[0])
    y = np.arange(image.shape[1])
    points = np.stack(list(product(x, y)))
    z = np.array([image[pt[0], pt[1]] for pt in points]).flatten() * z_multiplier
    z = z - z.min()

    tri = spatial.Delaunay(points)

    points_mesh = np.zeros((points.shape[0], 3))
    points_mesh[:, 1:] = points
    points_mesh[:, 0] = -z

    return (points_mesh, tri.simplices)
