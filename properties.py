import bpy


class GAOps_Properties(bpy.types.PropertyGroup):
    exe_path: bpy.props.StringProperty(
        name="SubstancePainter Exe",
        subtype="FILE_PATH",
    )
