import bpy
import bmesh


class OBJECT_OT_toggle_backface_culling(bpy.types.Operator):
    bl_idname = "gaops.toggle_backface_culling"
    bl_label = "Toggle backface culling"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if context.mode != "OBJECT":
            return False
        for obj in context.selected_objects:
            if obj.type == "MESH":
                return True
        return False

    def execute(self, context):
        obj_as_mesh = [obj for obj in context.selected_objects if obj.type == "MESH"]

        for obj in obj_as_mesh:
            for slot in obj.material_slots:
                if slot.material:
                    slot.material.use_backface_culling = (
                        not slot.material.use_backface_culling
                    )

        return {"FINISHED"}
