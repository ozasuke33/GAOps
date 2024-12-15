import bpy
import subprocess
import pathlib


class OBJECT_OT_launch_substance_painter(bpy.types.Operator):
    bl_idname = "gaops.launch_substance_painter"
    bl_label = "Launch Substance Painter with selected meshes"
    bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context):
        if bpy.context.preferences.addons["GAOps"].preferences.exe_path == "":
            return False
        if bpy.data.is_saved == False:
            return False
        for obj in context.selected_objects:
            if obj.type == "MESH":
                return True
        return False

    def execute(self, context):
        filename = str(pathlib.Path(bpy.path.abspath("//")) / "exchange.fbx")

        bpy.ops.export_scene.fbx(filepath=filename)

        subprocess.run(
            [
                bpy.context.preferences.addons["GAOps"].preferences.exe_path,
                "--mesh",
                filename,
            ]
        )
        return {"FINISHED"}
