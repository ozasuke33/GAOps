import bpy

class OBJECT_OT_facesets_to_vertexcolor(bpy.types.Operator):
    bl_idname = "gaops.facesets_to_vertexcolor"
    bl_label = "Face Sets to Vertex Color"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        return {"FINISHED"}