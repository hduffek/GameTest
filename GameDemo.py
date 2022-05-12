# Original Idea: https://youtu.be/T_HMm8Tn4f8
# Things Added: Shaders, Blocks/Objects, New Sky, Weapon, and Ground Textures

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader


set = Ursina()

# Sets sky texture and enables first person capabilities
Sky(texture="sky_sunset")
player = FirstPersonController()

# Practice model
block_1 = Entity(
    model='cube',
    texture='brick',
    collider='cube',
    color=color.orange,
    scale=2,
    position=(10, 1, 10),
    shader=lit_with_shadows_shader
)

block_2 = Entity(
    model='cube',
    texture='brick',
    collider='cube',
    color=color.red,
    scale=3,
    position=(10, 1, 7),
    shader=lit_with_shadows_shader
)

block_3 = Entity(
    model='cube',
    texture='brick',
    collider='cube',
    color=color.blue,
    scale=4,
    position=(7, 1, 10),
    shader=lit_with_shadows_shader
)

# Light entity
pivot = Entity()
DirectionalLight(parent=pivot, y=3, z=2, shadows=True)

# Variable for platforms to be added to
blocks = []

# Creates Player Entity and sets height on y-axis
player = Entity(
    model='cube',
    color=color.black,
    scale_y=2
)

# Gives movement to player
player.x += held_keys['d'] * .1
player.x -= held_keys['a'] * .1

# Creates a held entity, a sword in this case
sword = Entity(
    parent=camera.ui,
    model='cube',
    texture='sword',
    position=Vec2(0.406, -0.42))

# For loop creating textured tiles to send to 'blocks' variable
for z in range(20):
    for x in range(20):
        block = Button(
            color=color.white,
            model='cube',
            position=(x, 0, z),
            texture='grass',
            parent=scene,
            origin_y=0.5)
        blocks.append(block)

set.run()
