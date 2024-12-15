import bpy


class UI_PT_GAOps_Preferences(bpy.types.AddonPreferences):
    bl_idname = __package__

    exe_path: bpy.props.StringProperty(name="SubstancePainter Exe", subtype="FILE_PATH")

    def draw(self, context):
        layout = self.layout

        layout.prop(self, "exe_path")
