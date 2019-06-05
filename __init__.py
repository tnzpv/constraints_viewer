"""
  contraints_viewer allows to show all constraints between different armatures or objects in scene
"""

import bpy

from . import ui
from . import operators

bl_info = {
    "name": "Scene constraints viewer",
    "author": "TNZPV",
    "version": (1, 0),
    "blender": (2, 7, 9),
    "location": "3D View > Tool Shelf > Animation",
    "description": "Allows to see all the constraints between objects in scene",
    "category": "Animation"}


def register():
    bpy.utils.register_module(__name__)

    bpy.types.Scene.scene_constraints = bpy.props.CollectionProperty(type=ui.CstItem)
    bpy.types.Scene.active_scene_constraints = bpy.props.IntProperty()


def unregister():
    del bpy.types.Scene.scene_constraints
    del bpy.types.Scene.active_scene_constraints

    bpy.utils.unregister_module(__name__)
