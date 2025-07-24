import bpy
import bmesh

import random
import math


class OBJECT_OT_facesets_to_vertexcolor(bpy.types.Operator):
    bl_idname = "gaops.facesets_to_vertexcolor"
    bl_label = "Face Sets to Vertex Color"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        obj_as_mesh = []
        facesets_colors = []

        for obj in context.selected_objects:
            if obj.type == "MESH":
                obj_as_mesh.append(obj)

        active = context.view_layer.objects.active

        for obj in obj_as_mesh:
            context.view_layer.objects.active = obj
            bpy.ops.object.mode_set(mode="VERTEX_PAINT")

            facesets = {}
            bm = bmesh.new()
            bm.from_mesh(obj.data)

            layer_facesets = bm.faces.layers.int.get(".sculpt_face_set")
            if layer_facesets == None:
                break

            if (
                obj.data.attributes.active_color_index < 0
                or len(bm.loops.layers.color) == 0
            ):
                bm.loops.layers.color.new()
            layer_vertexcolor = bm.loops.layers.color[
                obj.data.attributes.active_color_index
            ]
            bpy.ops.geometry.color_attribute_render_set(name=layer_vertexcolor.name)

            for face in bm.faces:
                fs = face[layer_facesets]
                vertexcolor = [0, 0, 0]

                if fs not in facesets:
                    vertexcolor = [
                        random.random(),
                        random.random(),
                        random.random(),
                    ]
                    while True:
                        roll_dice = False
                        for _, color in facesets.items():
                            if (
                                math.isclose(color[0], vertexcolor[0], rel_tol=0.1)
                                and math.isclose(color[1], vertexcolor[1], rel_tol=0.1)
                                and math.isclose(color[2], vertexcolor[2], rel_tol=0.1)
                            ):
                                roll_dice = True

                        if roll_dice:
                            vertexcolor = [
                                random.random(),
                                random.random(),
                                random.random(),
                            ]
                        else:
                            break
                    facesets[fs] = vertexcolor

                if fs in facesets:
                    vertexcolor = facesets[fs]

                for loop in face.loops:
                    loop[layer_vertexcolor][0] = vertexcolor[0]
                    loop[layer_vertexcolor][1] = vertexcolor[1]
                    loop[layer_vertexcolor][2] = vertexcolor[2]

            bm.to_mesh(obj.data)
            bm.free()

        context.view_layer.objects.active = active

        return {"FINISHED"}
