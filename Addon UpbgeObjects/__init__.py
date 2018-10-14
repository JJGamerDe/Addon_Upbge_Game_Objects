"""
Copyright (C) 2018 Rafael Tavares
endssgamesstudio@bol.com.br

Created by Rafael Tavares

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

bl_info = {
    "name": "Upbge Game Objects",
    "author": "EndSSGames",
    "version": (0, 2),
    "blender": (2, 79, 6),
    "location": "View3D > Tools > Upbge Game Objects Panel",
    "description": "adds several game objects",
    "warning": "",
    "wiki_url": "https://github.com/EndSSgamesStudio/Addon_Upbge_Game_Objects",
    "tracker_url": "https://github.com/EndSSgamesStudio/Addon_Upbge_Game_Objects/issues",
    "category": "Game Engine"}

import bpy, imp
from math import *
import os


#from . import defs_game_objects
from . import class_game_objects

####################################################################################################	
class UpbgeGameObjectsPanel(bpy.types.Panel):
	"""Docstring of UpbgeGameObjectsPanel"""
	bl_idname = "VIEW3D_PT_upbge_game_objects"
	bl_label = "Upbge Game Objects Panel"
	
	bl_space_type = 'VIEW_3D'
	bl_region_type = 'TOOLS'
	bl_category = 'Tools'
	
	def draw(self, context):
		layout = self.layout
		
		#row = layout(aling = true)
		layout.operator(class_game_objects.PlayerFpsOperator.bl_idname, text = "FPS PLAYER", icon = 'ARMATURE_DATA')
		#row = layout.row(
		layout.operator(class_game_objects.ZombieOperator.bl_idname, text = "Zombie",icon = 'POSE_DATA')
		#ZombieOperator.bl_idname
		layout.operator(class_game_objects.FreeCameraOperator.bl_idname, text = "Free Camera",icon = 'SCENE')
		#Orbit
		layout.operator(class_game_objects.CameraOrbitOperator.bl_idname, text = "Camera Orbit",icon = 'CAMERA_DATA')
		#Third
		layout.operator(class_game_objects.ThirdpersonplayerOperator.bl_idname, text = "Third Person Player",icon = 'OUTLINER_DATA_ARMATURE')
		
		
		
	
####################################################################################################
    
    
        
def register():
    bpy.utils.register_module(__name__)
	
def unregister():

    bpy.utils.unregister_module(__name__)
    
if __name__ == "__main__":
    register()
    
    
	
    #PlayerFpsOperator