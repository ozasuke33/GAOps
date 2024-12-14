import bpy
import bmesh
import mathutils

import random

class OBJECT_OT_facesets_to_vertexcolor(bpy.types.Operator):
    bl_idname = "gaops.facesets_to_vertexcolor"
    bl_label = "Face Sets to Vertex Color"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):

        facesets = {}
        obj_as_mesh = []

        for obj in context.selected_objects:
            if obj.type == "MESH":
                obj_as_mesh.append(obj)

        for obj in obj_as_mesh:
            bm = bmesh.new()
            bm.from_mesh(obj.data)

            layer_facesets = bm.faces.layers.int.get('.sculpt_face_set')
            if layer_facesets == None:
                break

            layer_vertexcolor = bm.loops.layers.color[0]

            for face in bm.faces:
                fs = face[layer_facesets]
                vertexcolor = [0, 0, 0]
                if fs not in facesets:
                    vertexcolor = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
                    while True:
                        roll_dice = False
                        for _, color in facesets.items():
                            if color[0] == vertexcolor[0] and color[1] == vertexcolor[1] and color[2] == vertexcolor[2]:
                                roll_dice = True
                        if roll_dice:
                            vertexcolor = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
                        else:
                            break
                    facesets[fs] = vertexcolor
                if fs in facesets:
                    vertexcolor = facesets[fs]

                for loop in face.loops:
                    loop[layer_vertexcolor][0] = vertexcolor[0] / 255.0
                    loop[layer_vertexcolor][1] = vertexcolor[1] / 255.0
                    loop[layer_vertexcolor][2] = vertexcolor[2] / 255.0

            bm.to_mesh(obj.data)
            bm.free()

        return {"FINISHED"}