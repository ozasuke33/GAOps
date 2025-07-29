import bpy


class UI_PT_create_stylized_bush(bpy.types.Panel):
    bl_idname = "UI_PT_create_stylized_bush"
    bl_label = "Create Stylized Bush"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "GAOps"

    def draw(self, context):
        layout = self.layout

        layout.operator("gaops.create_stylized_bush")