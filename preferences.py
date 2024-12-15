import bpy


class UI_PT_GAOps_Preferences(bpy.types.AddonPreferences):
    bl_idname = __package__

    def draw(self, context):
        layout = self.layout

        layout.prop(context.window_manager.gaops_properties, "exe_path")
