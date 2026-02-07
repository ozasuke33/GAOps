import bpy

export_format_items = [
    ("GLB", "glTF Binary(.glb)", ""),
    ("GLTF_SEPARATE", "glTF Separate(.gltf + .bin + textures)", ""),
    ("FBX", "FBX(.fbx + textures)", ""),
]


class PropertyGroup_batch_export(bpy.types.PropertyGroup):

    export_format: bpy.props.EnumProperty(
        items=export_format_items, default="GLB", name="Export Format"
    )

    export_path: bpy.props.StringProperty(
        name="Export Path",
        default=bpy.app.tempdir,
        subtype="DIR_PATH",
        options={"PATH_SUPPORTS_BLEND_RELATIVE"},
    )
