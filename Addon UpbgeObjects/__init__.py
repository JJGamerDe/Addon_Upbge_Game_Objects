'''
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
'''

bl_info = {
    "name": "Upbge Game Objects",
    "author": "RafaelTavares(EndSSGames)",
    "version": (0, 1),
    "blender": (2, 79, 6),
    "location": "View3D > Tools > Upbge Objects",
    "description": "adds several game objects for free use",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "UPBGE"}

import bpy
from math import *
import os
############################################
class PlayerFpsOperator(bpy.types.Operator):
    #"""ToolTip of UpbgeGameObjectsOperator"""
    bl_idname = "player.objects_operator"
    bl_label = "Upbge Game Objects"
    bl_description = 'Generate a FPS PLAYER'
    bl_options = {'REGISTER', "UNDO"}
 
    def execute(self, context):
        self.report({'INFO'}, "Sucess!")
        
        PlayerFps()
        
        return {'FINISHED'}
    
    #def executeZombie(self, context,):
        #self.report({'INFO'}, "Sucess!")
        
        #Zombie()
        
        #return {'FINISHED'}
#########################################		
class ZombieOperator(bpy.types.Operator):
    bl_idname = "zombie.objects_operator"
    bl_label = "Upbge Game Objects"
    bl_description = "Generate a Zombie"
    bl_options = {'REGISTER', "UNDO"}
	
    
    def execute(self, context):
        self.report({'INFO'}, "Sucess!!")
        
        Zombie()
        
        return {'FINISHED'}
#########################################
class FreeCameraOperator(bpy.types.Operator):
    bl_idname = "freecamera.objects_operator"
    bl_label = "Upbge Game Objects"
    bl_description = "Generate a free camera"
    bl_options = {'REGISTER', "UNDO"}
	
    
    def execute(self, context):
        self.report({'INFO'}, "Sucess!!")
        
        FreeCamera()
        
        return {'FINISHED'}
    
#########################################
class CameraOrbitOperator(bpy.types.Operator):
    bl_idname = "orbitcamera.objects_operator"
    bl_label = "Upbge Game Objects"
    bl_description = "Generate a Camera Orbital"
    bl_options = {'REGISTER', "UNDO"}
	
    
    def execute(self, context):
        self.report({'INFO'}, "Sucess!!")
        
        orbitcamera()
        
        return {'FINISHED'}

#####################################################################################	


def PlayerFps():
    
	obj = loadAsset('objects.blend', ('player_body', 'player_camera', 'player_head'))
	return obj

def Zombie():
    
	obj = loadAsset('objects.blend', ('Zombie'))
	return obj

def FreeCamera():
    
    obj = loadAsset('objects.blend', ('Free_CameraPlayer'))
    return obj

def orbitcamera():

    obj = loadAsset('objects.blend', ("Camera_Orbit", "Orbit_Camera"))
    return obj
    
    
#####################################################################################	
#####################################################################################	
def loadAsset(filename, objList):

	scriptPath = os.path.realpath(__file__)
	assetPath = os.path.join(os.path.dirname(scriptPath), 'asset', filename)

	try:
		with bpy.data.libraries.load(assetPath)	as (data_from, data_to):
			data_to.objects = [name for name in data_from.objects if name in objList]
	except:
		return 'What you mean? this asset does not exist!'

	retObj = None
	for obj in data_to.objects:
		bpy.context.scene.objects.link(obj)
		retObj = obj

	return retObj
####################################################################################################
####################################################################################################	
class UpbgeGameObjectsPanel(bpy.types.Panel):
    """Docstring of UpbgeGameObjectsPanel"""
    bl_idname = "VIEW3D_PT_upbge_game_objects"
    bl_label = "Upbge Game Objects Panel"
    
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = 'Tools'
    
####################################################################################################
    def draw(self, context):
        layout = self.layout
		
		#row = layout.row(align = True)
        layout.operator(PlayerFpsOperator.bl_idname, text = "FPS PLAYER", icon = 'ARMATURE_DATA')
      	#row = layout.row()
        layout.operator(ZombieOperator.bl_idname, text = "Zombie",icon = 'POSE_DATA')
		#ZombieOperator.bl_idname
        layout.operator(FreeCameraOperator.bl_idname, text = "Free Camera",icon = 'SCENE')
        #boing
        layout.operator(CameraOrbitOperator.bl_idname, text = "Camera Orbit",icon = 'CAMERA_DATA')
    
        
def register():
    bpy.utils.register_module(__name__)
    #bpy.utils.register_class(PlayerFpsOperator)
	#bpy.utils.register_class(ZombieOperator)
    #bpy.utils.register_class(UpbgeGameObjectsPanel)
def unregister():
    bpy.utils.unregister_module(__name__)
    #bpy.utils.unregister_class(PlayerFpsOperator)
	#bpy.utils.unregister_class(ZombieOperator)
    #bpy.utils.unregister_class(UpbgeGameObjectsPanel)
    
if __name__ == "__main__":
    register()
    
    
    #PlayerFpsOperator