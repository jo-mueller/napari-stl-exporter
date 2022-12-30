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
def image_to_surface(image: ImageData,
                     z_multiplier: float = 1.0,
                     solidify: bool = True) -> SurfaceData:
    """
    Convert a 2D image to a surface mesh. The image intensity is used as z-coordinate of the mesh.

    Parameters
    ----------
    image : ImageData
    z_multiplier: float
        Multiplies the intensity-derived z-coordinate with this factor.
    solidify: bool
        Whether or not to extrude the mesh by an automatically
        determined value to turn it into a solid (printable) object.

    
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

    surface = (points_mesh, tri.simplices)

    if solidify:

        # extrude mesh by maximum z-value * -1 and set all values of the extruded
        # vertices to the same value to create a flat bottom.
        extrude_distance = points_mesh[:, 0].max()
        extruded_surface = list(extrude(surface, -extrude_distance))

        extrude_surface[0][len(surface) + 1:] = -0.1
        surface = extruded_surface


    return surface
