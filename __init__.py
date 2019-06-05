"""
  contraints_viewer allows to show all constraints between different armatures or objects in scene
    Copyright (C) 2019 TNZPV

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
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
