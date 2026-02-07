import bpy


class UI_PT_batch_export(bpy.types.Panel):
    bl_idname = "UI_PT_batch_export"
    bl_label = "Batch Export"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "GAOps"

    def draw(self, context):
        layout = self.layout

        layout.prop(context.window_manager.GAOps_batch_export, "export_format")
        layout.prop(context.window_manager.GAOps_batch_export, "export_path")
        op = layout.operator("gaops.batch_export", icon="EXPORT")

        if context.window_manager.GAOps_batch_export.export_format == "GLB":
            op.is_glb = True
        else:
            op.is_glb = False
        
        if context.window_manager.GAOps_batch_export.export_format == "FBX":
            op.is_fbx = True

        op.path = context.window_manager.GAOps_batch_export.export_path
