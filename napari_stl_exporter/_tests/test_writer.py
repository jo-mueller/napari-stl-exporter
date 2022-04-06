from napari_stl_exporter._writer import _labels_to_mesh, napari_write_labels, napari_write_surface
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
