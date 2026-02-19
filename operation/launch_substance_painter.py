import bpy
import subprocess
import pathlib


class OBJECT_OT_launch_substance_painter(bpy.types.Operator):
    bl_idname = "gaops.launch_substance_painter"
    bl_label = "Launch Substance Painter with selected meshes"
    bl_description = "Launch Substance Painter with selected meshes (You need to set the path of Substance Painter EXE in preferences)"
    bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context):
        if bpy.context.preferences.addons["GAOps"].preferences.exe_path == "":
            return False

        for obj in context.selected_objects:
            if obj.type == "MESH":
                return True
        return False

    def execute(self, context):
        filename = str(
            pathlib.Path(bpy.path.abspath(bpy.app.tempdir)) / "gaops_exchange.fbx"
        )

        bpy.ops.export_scene.fbx(
            filepath=filename, use_selection=True, use_mesh_modifiers=True
        )

        subprocess.Popen(
            [
                bpy.context.preferences.addons["GAOps"].preferences.exe_path,
                "--mesh",
                filename,
            ]
        )
        return {"FINISHED"}
