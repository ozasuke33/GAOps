import bpy


class UI_PT_toggle_backface_culling(bpy.types.Panel):
    bl_idname = "UI_PT_toggle_backface_culling"
    bl_label = "Toggle backface culling"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "GAOps"

    def draw(self, context):
        layout = self.layout

        layout.operator("gaops.toggle_backface_culling", icon="MATERIAL")
