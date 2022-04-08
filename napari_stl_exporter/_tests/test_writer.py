from napari_stl_exporter._writer import _labels_to_mesh, napari_write_labels, napari_write_surface
from napari_stl_exporter._test_data import make_pyramid_label, make_pyramid_surface, make_landscape
from napari_stl_exporter._image_to_surface import image_to_surface

import numpy as np
import os

def test_label_conversion():
    import vedo
    label_image = np.zeros((100, 100, 100))
    label_image[25:75, 25:75, 25:75] = 1

    mesh = _labels_to_mesh(label_image)

    assert isinstance(mesh, vedo.mesh.Mesh)

def test_writer(tmpdir):
    from skimage import measure
    label_image = np.zeros((100, 100, 100))
    label_image[25:75, 25:75, 25:75] = 1

    pth = os.path.join(str(tmpdir), "test_export.stl")
    stl_file = napari_write_labels(pth, label_image, None)
    assert os.path.exists(pth)
    assert stl_file is not None

    pth = os.path.join(str(tmpdir), "test_export.ply")
    ply_file = napari_write_labels(pth, label_image, None)
    assert os.path.exists(pth)
    assert ply_file is not None

    surf = measure.marching_cubes(label_image)

    pth = os.path.join(str(tmpdir), "test_export.ply")
    stl_file = napari_write_surface(pth, surf, None)
    assert os.path.exists(pth)
    assert stl_file is not None

    pth = os.path.join(str(tmpdir), "test_export.stl")
    stl_file = napari_write_surface(pth, surf, None)
    assert os.path.exists(pth)
    assert stl_file is not None

def test_writer_viewer(make_napari_viewer, tmpdir):
    import napari
    # Load and binarize image
    label_image = np.zeros((100, 100, 100), dtype=int)
    label_image[25:75, 25:75, 25:75] = 1

    # Add data to viewer
    viewer = make_napari_viewer()
    label_layer = viewer.add_labels(label_image, name='3D object')

    # save the layer as 3D printable file to disc
    napari.save_layers(os.path.join(tmpdir, 'test.stl'), [label_layer])
    assert os.path.exists(os.path.join(tmpdir, 'test.stl'))

def test_sample_data(make_napari_viewer, tmpdir):
    label_image = make_pyramid_label()
    assert label_image is not None

    surface_image = make_pyramid_surface()
    assert surface_image is not None

    landscape = make_landscape()

    widget = image_to_surface()
    surf = widget(landscape[0][0], z_multiplier=0.25)

    viewer = make_napari_viewer()
    viewer.add_surface(surf)

    assert len(viewer.layers) == 1
