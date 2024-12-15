import bpy


class UI_PT_launch_substance_painter(bpy.types.Panel):
    bl_idname = "UI_PT_launch_substance_painter"
    bl_label = "Launch Substance Painter with selected meshes"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "GAOps"

    def draw(self, context):
        layout = self.layout

        layout.operator("gaops.launch_substance_painter")
