import pyglet
from pyglet import window, app, shapes
from pyglet.window import mouse,key

from pyglet.graphics.shader import Shader, ShaderProgram
from pyglet.gl import GL_TRIANGLES
from pyglet.math import Mat4, Vec3
from pyglet.gl import *

import shader
from primitives import CustomGroup

class RenderWindow(pyglet.window.Window):
    '''
    inherits pyglet.window.Window which is the default render window of Pyglet
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.batch = pyglet.graphics.Batch()
        self.lookat = Vec3(0,2,3)
        self.num_shape =0
        self.z_near = 0.1
        self.z_far = 100
        self.fov = 60
        self.view = Mat4.look_at(self.lookat, target=Vec3(0,0,0), up=Vec3(0,1,0))
        self.proj_mat = None

        self.setup()

    def setup(self) -> None:
        self.set_minimum_size(width = 400, height = 300)
        self.set_mouse_visible(False)
        glEnable(GL_DEPTH_TEST)

        # 1. create the view and (orthographic) projection matrices
        # LookAt matrix
        self.view = Mat4.look_at(self.lookat, target=Vec3(0,0,0), up=Vec3(0,1,0))
        
        # #orthographic projectic matrices
        # proj_mat = Mat4.orthogonal_projection(left=0, right=width, bottom=0, top=height, z_near=0.1, z_far=1000)
        # 1-1 for the persepective projection
        self.proj_mat = Mat4.perspective_projection(aspect = self.width/self.height, z_near=self.z_near, z_far=self.z_far, fov = self.fov)
        # 2. combine the view and projection matrices into one matrix
        vp = self.proj_mat @ self.view
        # 3. upload the combined view-projection matrix to the vertex shader vp uniform
        shader.program['vp'] = vp

    def on_draw(self) -> None:
        self.clear()
        self.batch.draw()

    def update(self,dt) -> None:
        translate_mat = Mat4.from_translation(vector=Vec3(x=0,y=0,z=0))
        rotate_mat = Mat4.from_rotation(angle=0, vector=Vec3(0,1,0))
        model_mat = translate_mat @ rotate_mat
        shader.program['model'] = model_mat

    def on_resize(self, width, height):
       glViewport(0,0,width, height)
       self.projection = Mat4.perspective_projection(self.aspect_ratio, z_near=0.1, z_far=255, fov = 60) #1280/720 = 1.7777
       return pyglet.event.EVENT_HANDLED

    def add_shape(self, pos, vertice,indice, color):    
        custom_group = CustomGroup(self.num_shape,shader.program, pos, Vec3(0,0,1))
        shader.program.vertex_list_indexed(len(vertice)//3, GL_TRIANGLES,
                        batch = self.batch,
                        group = custom_group,
                        indices = indice,
                        vertices = ('f', vertice),
                        colors = ('Bn', color)) 
        
        self.num_shape+=1
         
    def run(self):
        pyglet.clock.schedule_interval(self.update, 1/60)
        pyglet.app.run()
    