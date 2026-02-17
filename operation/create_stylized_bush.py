import bpy
import bmesh


class OBJECT_OT_create_stylized_bush(bpy.types.Operator):
    bl_idname = "gaops.create_stylized_bush"
    bl_label = "Create Stylized Bush"
    bl_options = {"REGISTER", "UNDO"}

    voxel_size: bpy.props.FloatProperty(
        name="Voxel Size",
        description="Size of the voxel in object space used for volume evaluation. Lower values preserve finer details.",
        default=0.1,
        min=0.05,
    )

    scale: bpy.props.FloatProperty(
        name="Face Scale", description="Scale of Faces", default=1.0
    )

    amount: bpy.props.FloatProperty(
        name="Amount", description="Amount, Distance to offset", default=0.1, min=0
    )

    seed: bpy.props.IntProperty(
        name="Seed",
        description="Random Seed, Seed for the random number generator",
        default=0,
        min=0,
        max=10000,
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
            if obj.type != "MESH":
                obj.select_set(False)
            if obj.type == "MESH":
                obj_as_mesh.append(obj)

        for obj in obj_as_mesh:
            context.view_layer.objects.active = obj
            if not "Remesh" in obj.modifiers:
                bpy.ops.object.modifier_add(type="REMESH")
            obj.modifiers["Remesh"].voxel_size = self.voxel_size

        bpy.ops.object.duplicate_move()

        bpy.ops.object.convert(target="MESH")

        bpy.ops.object.mode_set(mode="EDIT")

        bpy.ops.mesh.bevel(
            offset_type="PERCENT", offset_pct=25.0, segments=2, profile=1.0
        )

        bpy.ops.mesh.select_all(action="SELECT")

        bpy.ops.mesh.edge_split(type="EDGE")

        prev_pivot = context.tool_settings.transform_pivot_point
        context.tool_settings.transform_pivot_point = "INDIVIDUAL_ORIGINS"

        bpy.ops.transform.resize(value=(self.scale, self.scale, self.scale))

        context.tool_settings.transform_pivot_point = prev_pivot

        bpy.ops.transform.vertex_random(offset=self.amount, seed=self.seed)

        bpy.ops.object.mode_set(mode="OBJECT")

        return {"FINISHED"}
