from importlib import reload
import sys
import bpy

from .operation import facesets_to_vertexcolor
from .operation import launch_substance_painter


def reload_modules():
    if not bpy.context.preferences.view.show_developer_ui:
        return

    reload(sys.modules[__name__])
    reload(facesets_to_vertexcolor)
    reload(launch_substance_painter)
