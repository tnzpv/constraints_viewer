import bpy

class CstItem(bpy.types.PropertyGroup):
    """ Item in UIList """
    '''name = bpy.props.StringProperty()'''
    id = bpy.props.IntProperty()


class CstsItems(bpy.types.UIList):
    """ UIList of assets in popup """

    def draw_item(self, context, layout, data, item, icon, active_data, active_propname):
        split = layout.split(0.8)
        split.prop(item, "name", text="", emboss=False, translate=False, icon='BORDER_RECT')

class ConstraintsViewer(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = 'Animation'
    bl_label = "Constraints Viewer"
    bl_idname = "show_scene_constraints"

    @classmethod
    def poll(cls, context):
        return context.scene

    def draw(self, context):
        layout = self.layout.column(align=True)
        rows = 2
        row = layout.row()
        col = row.column(align=True)
        col.operator("scene_constraints.show_constraints", text='Show Scene Constraints')
        row = layout.row()
        row.template_list("CstsItems", " ", context.scene,
                          "scene_constraints", context.scene,
                          "active_scene_constraints", rows=rows)
