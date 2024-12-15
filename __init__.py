bl_info = {
    "name": "GAOps",
    "author": "ozasuke",
    "description": "Game Asset Operations",
    "blender": (4, 3, 0),
    "version": (0, 0, 1),
    "location": "3D Vieport > Sidebar",
    "warning": "",
    "category": "Object",
}

import bpy

from . import _refresh_

_refresh_.reload_modules()

from .operation.facesets_to_vertexcolor import *
from .operation.launch_substance_painter import *
from .preferences import *
from .panel.pt_facesets_to_vertexcolor import *
from .panel.pt_launch_substance_painter import *

classess = [
    OBJECT_OT_facesets_to_vertexcolor,
    OBJECT_OT_launch_substance_painter,
    UI_PT_GAOps_Preferences,
    UI_PT_faceSets_to_vertexcolor,
    UI_PT_launch_substance_painter,
]


def register():
    for cls in classess:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classess:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
