import numpy as np
import os
import vedo

supported_surface_formats = ['.stl', '.ply', '.obj']
supported_points_formats = ['.vtp']


def test_label_conversion():
    import vedo
    from napari_stl_exporter._writer import _labels_to_mesh, napari_write_labels, napari_write_surfaces
    label_image = np.zeros((100, 100, 100))
    label_image[25:75, 25:75, 25:75] = 1

    mesh = _labels_to_mesh(label_image)

    assert isinstance(mesh, vedo.mesh.Mesh)


def test_writer(tmpdir):
    from skimage import measure
    import pandas as pd
    from napari_stl_exporter._writer import (
        napari_write_labels,
        napari_write_surfaces,
        napari_write_points)

    label_image = np.zeros((100, 100, 100))
    label_image[25:75, 25:75, 25:75] = 1

    points_data_3d = np.random.rand(100, 3)
    points_data_3d_features = pd.DataFrame(
        np.random.rand(100, 3),
        columns=['feat1', 'feat2', 'feat3'])

    for ext in supported_surface_formats:
        pth = os.path.join(str(tmpdir), "test_export" + ext)
        stl_file = napari_write_labels(pth, label_image, None)
        assert os.path.exists(pth)
        assert stl_file is not None

    surf = measure.marching_cubes(label_image)

    for ext in supported_surface_formats:
        pth = os.path.join(str(tmpdir), "test_export" + ext)
        stl_file = napari_write_surfaces(pth, surf, None)
        assert os.path.exists(pth)
        assert stl_file is not None

    for ext in supported_points_formats:
        pth = os.path.join(str(tmpdir), "test_export" + ext)
        vtp_file3d = napari_write_points(
            pth,
            points_data_3d,
            {'features': points_data_3d_features})
        assert os.path.exists(pth)
        assert vtp_file3d is not None


def test_writer_viewer(make_napari_viewer, tmpdir):
    import napari
    import pandas as pd
    # Load and binarize image
    label_image = np.zeros((100, 100, 100), dtype=int)
    points_data_3d = np.random.rand(100, 3)
    points_data_3d_features = pd.DataFrame(
        np.random.rand(100, 3),
        columns=['feat1', 'feat2', 'feat3'])
    label_image[25:75, 25:75, 25:75] = 1

    # Add data to viewer
    viewer = make_napari_viewer()
    label_layer = viewer.add_labels(label_image, name='3D object')
    points_layer = viewer.add_points(points_data_3d, name='3D points',
                                     features=points_data_3d_features)

    # save the layer as 3D printable file to disc
    napari.save_layers(os.path.join(tmpdir, 'test.stl'), [label_layer])
    napari.save_layers(os.path.join(tmpdir, 'test.vtp'), [points_layer])
    assert os.path.exists(os.path.join(tmpdir, 'test.stl'))


def test_sample_data():
    from napari_stl_exporter._sample_data import make_pyramid_label, make_pyramid_surface
    label_image = make_pyramid_label()
    assert label_image is not None

    surface_image = make_pyramid_surface()
    assert surface_image is not None


def test_reader(make_napari_viewer, tmpdir):
    import napari_stl_exporter
    import pandas as pd
    from napari_stl_exporter._sample_data import make_pyramid_surface
    from napari_stl_exporter._writer import napari_write_surfaces, napari_write_points
    from napari_stl_exporter._reader import napari_import_surface, napari_import_points

    points_data_3d = np.random.rand(100, 3)
    points_data_3d_features = pd.DataFrame(
        np.random.rand(100, 3),
        columns=['feat1', 'feat2', 'feat3'])

    pyramid = napari_stl_exporter.make_pyramid_surface()[0][0]
    viewer = make_napari_viewer()

    for ext in supported_surface_formats:
        path = os.path.join(tmpdir, 'test' + ext)
        napari_write_surfaces(path, pyramid, None)
        _pyramid = napari_import_surface(path)[0]
        viewer.add_surface(_pyramid[0], **_pyramid[1])

        # make sure that a reader is found
        reader = napari_stl_exporter._reader.get_reader(path)
        data = reader(path)
        assert data is not None

    for ext in supported_points_formats:
        path = os.path.join(tmpdir, 'test' + ext)
        napari_write_points(path, points_data_3d, {'features': points_data_3d_features})
        _points = napari_import_points(path)[0]

        layer = viewer.add_points(_points[0], **_points[1])
        assert hasattr(layer, 'features')


def test_image_surface_conversion():
    from skimage import data
    from napari_stl_exporter._image_to_surface import image_to_surface

    image = data.cell()
    surface = image_to_surface(image)


def test_widgets(make_napari_viewer):
    from napari_stl_exporter._image_to_surface import image_to_surface_widget, extrude_widget
    
    viewer = make_napari_viewer()

    widget_surface = image_to_surface_widget()
    widget_extrude = extrude_widget()

    viewer.window.add_dock_widget(widget_surface)
    viewer.window.add_dock_widget(widget_extrude)
