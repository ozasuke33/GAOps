import bpy
import bmesh

import pathlib

export_format_items = [
    ("GLB", "glTF Binary(.glb)", ""),
    ("GLTF_SEPARATE", "glTF Separate(.gltf + .bin + textures)", ""),
    ("FBX", "FBX(.fbx + textures)", ""),
]


class OBJECT_OT_batch_export(bpy.types.Operator):
    bl_idname = "gaops.batch_export"
    bl_label = "Batch Export"
    bl_options = {"REGISTER"}

    export_format: bpy.props.EnumProperty(
        items=export_format_items, default="GLB", name="Export Format"
    )

    path: bpy.props.StringProperty(
        name="Export Path",
        default=bpy.app.tempdir,
        subtype="DIR_PATH",
        options={"PATH_SUPPORTS_BLEND_RELATIVE"},
    )

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
            if obj.type == "MESH" or obj.type == "EMPTY":
                obj_as_mesh.append(obj)

        for obj in obj_as_mesh:

            parent_in_selected_objects = False
            parent = obj.parent
            while parent:
                if parent in obj_as_mesh:
                    parent_in_selected_objects = True
                parent = parent.parent

            if parent_in_selected_objects:
                continue

            prev_loc = obj.location.copy()

            obj.location = (0, 0, 0)

            for c in obj.children_recursive:
                if c in obj_as_mesh:
                    c.select_set(True)
            obj.select_set(True)

            if self.path == "":
                self.path = bpy.app.tempdir
            if self.path.startswith("//") and not bpy.data.is_saved:
                self.path = bpy.app.tempdir

            if self.export_format == "FBX":

                filename = str(
                    pathlib.Path(bpy.path.abspath(self.path)) / (obj.name + ".fbx")
                )

                bpy.ops.export_scene.fbx(
                    filepath=filename,
                    use_selection=True,
                    path_mode="COPY",
                    use_mesh_modifiers=True,
                    use_triangles=True,
                    use_custom_props=True,
                    apply_scale_options="FBX_SCALE_ALL",
                )

            elif self.export_format == "GLB":

                filename = str(
                    pathlib.Path(bpy.path.abspath(self.path)) / (obj.name + ".glb")
                )

                bpy.ops.export_scene.gltf(
                    filepath=filename,
                    use_selection=True,
                    export_apply=True,
                    export_format="GLB",
                    export_tangents=True,
                    export_extras=True,
                )
            else:

                filename = str(
                    pathlib.Path(bpy.path.abspath(self.path)) / (obj.name + ".gltf")
                )

                bpy.ops.export_scene.gltf(
                    filepath=filename,
                    use_selection=True,
                    export_apply=True,
                    export_format="GLTF_SEPARATE",
                    export_tangents=True,
                    export_extras=True,
                )

            # bpy.ops.wm.obj_export(
            #    filepath=filename,
            #    export_selected_objects=True,
            #    export_triangulated_mesh=True,
            #    export_pbr_extensions=True,
            #    path_mode="COPY",
            # )

            for c in obj.children_recursive:
                if c in obj_as_mesh:
                    c.select_set(False)
            obj.select_set(False)

            obj.location = prev_loc

        self.report({"INFO"}, f"Batch exported to {bpy.path.abspath(self.path)}")
        return {"FINISHED"}
