# File created by: Zander Collins

# testing changes

# import libraries
# test comment for git
import pygame as pg
import random
import os
from os import path

# import settings
from settings import *
from sprites import *
from random import randint
# from pg.sprite import Sprite

class Game: 
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH,HEIGHT)) 
        pg.display.set_caption("My Game")
        self.clock = pg.time.Clock()
        self.running = True

    def new(self):
            self.score = 0 
            self.all_sprites = pg.sprite.Group()
            self.platforms = pg.sprite.Group() 
            self.enemies = pg.sprite.Group()
            self.player = Player(self)
            self.all_sprites.add(self.player)
            for i in range(1,10):
                e = Mob()
                self.all_sprites.add(e)
            self.run()

    def run(self):
        self.playing = True 
        while self.playing: 
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    def events():
        pass
    def update():
        pass
    def draw():
        pass
                



# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "Images")

def get_mouse_now():
    x,y = pg.mouse.get_pos()
    return (x,y)

vec = pg.math.Vector2 

# player is instantiated here

# game loop

while RUNNING:
    ### process input events section of game loop
    for event in pg.event.get():
        # check for window closing
        if event.type == pg.QUIT:
            RUNNING = False
            # break
    # print(get_mouse_now())
    ### update section of game loop (if updates take longer the 1/30th of a second, you will get laaaaag...)
    all_sprites.update()

    '''
    blocks_hit_list = pg.sprite.spritecollide(player, enemies, True)
    for block in blocks_hit_list:
        # print(enemies)
        pass
    '''
    ### draw and render section of game loop
    screen.fill(BLUE)
    all_sprites.draw(screen)
    # double buffering draws frames for entire screen
    pg.display.flip()
    # pg.display.update() -> only updates a portion of the screen
# ends program when loops evaluates to false
pg.quit()