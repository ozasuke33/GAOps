import bpy


class UI_PT_faceSets_to_vertexcolor(bpy.types.Panel):
    bl_idname = "UI_PT_faceSets_to_vertexcolor"
    bl_label = "Face Sets to Vertex Color"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "GAOps"

    def draw(self, context):
        layout = self.layout

        layout.operator("gaops.facesets_to_vertexcolor", icon="COLOR")
