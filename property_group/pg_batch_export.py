import bpy

class PropertyGroup_batch_export(bpy.types.PropertyGroup):
    export_path: bpy.props.StringProperty(
        name="Export Path",
        default=bpy.app.tempdir,
        subtype="DIR_PATH",
        options={'PATH_SUPPORTS_BLEND_RELATIVE'},
    )