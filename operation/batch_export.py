import bpy
import bmesh

import pathlib


class OBJECT_OT_batch_export(bpy.types.Operator):
    bl_idname = "gaops.batch_export"
    bl_label = "Batch Export"
    bl_options = {"REGISTER"}

    path: bpy.props.StringProperty(name="Export Path", default=bpy.app.tempdir, subtype="DIR_PATH", options={'PATH_SUPPORTS_BLEND_RELATIVE'})

    @classmethod
    def poll(cls, context):
        if context.mode != "OBJECT":
            return False
        for obj in context.selected_objects:
            if obj.type == "MESH":
                return True
        return False

    def execute(self, context):
        obj_as_mesh = []

        for obj in context.selected_objects:
            obj.select_set(False)
            if obj.type == "MESH":
                obj_as_mesh.append(obj)
        
        for obj in obj_as_mesh:
            prev_loc = obj.location.copy()

            obj.location = (0, 0, 0)

            obj.select_set(True)

            if self.path == "":
                self.path = bpy.app.tempdir
            if self.path.startswith("//") and not bpy.data.is_saved:
                self.path = bpy.app.tempdir

            filename = str(pathlib.Path(bpy.path.abspath(self.path)) / obj.name)

            bpy.ops.export_scene.gltf(filepath=filename, use_selection=True)

            obj.location = prev_loc
            
            obj.select_set(False)

        self.report({'INFO'}, f"Batch exported to {bpy.path.abspath(self.path)}")
        return {"FINISHED"}