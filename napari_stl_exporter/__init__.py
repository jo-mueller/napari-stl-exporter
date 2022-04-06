
__version__ = "0.0.6"

from ._writer import napari_get_writer, napari_write_labels, napari_write_surfaces
from napari_plugin_engine import napari_hook_implementation
from ._image_to_surface import image_to_surface

@napari_hook_implementation
def napari_experimental_provide_dock_widget():
    return image_to_surface
