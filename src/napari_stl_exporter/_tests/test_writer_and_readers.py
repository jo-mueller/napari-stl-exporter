from napari_stl_exporter._writer import _labels_to_mesh, napari_write_labels, napari_write_surfaces
from napari_stl_exporter import napari_import_surface
from napari_stl_exporter._sample_data import make_pyramid_label, make_pyramid_surface
import numpy as np
import os

supported_formats = ['.stl', '.ply', '.obj']

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

    for ext in supported_formats:
        pth = os.path.join(str(tmpdir), "test_export" + ext)
        stl_file = napari_write_labels(pth, label_image, None)
        assert os.path.exists(pth)
        assert stl_file is not None

    surf = measure.marching_cubes(label_image)

    for ext in supported_formats:
        pth = os.path.join(str(tmpdir), "test_export" + ext)
        stl_file = napari_write_surfaces(pth, surf, None)
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

def test_sample_data():
    label_image = make_pyramid_label()
    assert label_image is not None

    surface_image = make_pyramid_surface()
    assert surface_image is not None

def test_reader(make_napari_viewer, tmpdir):
    import napari_stl_exporter

    pyramid = napari_stl_exporter.make_pyramid_surface()[0][0]
    viewer = make_napari_viewer()

    for ext in supported_formats:
        path = os.path.join(tmpdir, 'test' + ext)
        napari_write_surfaces(path, pyramid, None)
        _pyramid = napari_import_surface(path)[0]
        viewer.add_surface(_pyramid[0], **_pyramid[1])

        # make sure that a reader is found
        reader = napari_stl_exporter._reader.get_reader(path)
        data = reader(path)
        assert data is not None


if __name__ == '__main__':
    import napari
    test_reader(napari.Viewer, r'C:\Users\johamuel\Desktop')
