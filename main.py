import pyglet
from pyglet.math import Mat4, Vec3

from render import RenderWindow
from primitives import Cube,Sphere
from control import Control


if __name__ == '__main__':
    width = 1280
    height = 720

    # render window.
    renderer = RenderWindow(width,height, "Hello Pyglet", resizable = True)   
    # renderer.set_location(200,1200)

    # Keyboard/Mouse control. Not implemented yet.
    controller = Control(renderer)

    translate_mat1 = Mat4.from_translation(vector=Vec3(x=-2, y=0,z=0))
    translate_mat2 = Mat4.from_translation(vector=Vec3(x=0, y=0,z=0))
    translate_mat3 = Mat4.from_translation(vector=Vec3(x=2, y=0,z=0))

    scale_vec = Vec3(x=1, y=1, z=1)

    cube1 = Cube(scale_vec)
    cube2 = Cube(Vec3(x=1.5, y=1.5, z=1.5))
    sphere = Sphere(30,30)
    renderer.add_shape(translate_mat1, cube1.vertices, cube1.indices, cube1.colors)
    renderer.add_shape(translate_mat2, sphere.vertices, sphere.indices, sphere.colors)
    renderer.add_shape(translate_mat3, cube2.vertices, cube1.indices, cube1.colors)

    #draw shapes
    renderer.run()
