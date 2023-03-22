# File created by: Zander Collins

import pygame as pg

from pygame.sprite import Sprite

from settings import *

import os 

from os import path

vec = pg.math.Vector2


game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "Images")


# create a player

class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((50,50))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.cofric = 0.1
        self.canjump = False
    def input(self):
        keystate = pg.key.get_pressed()
        if keystate[pg.K_w]:
            self.acc.y = -PLAYER_ACC
        if keystate[pg.K_a]:
            self.acc.x = -PLAYER_ACC
        if keystate[pg.K_s]:
            self.acc.y = PLAYER_ACC
        if keystate[pg.K_d]:
            self.acc.x = PLAYER_ACC
    def update(self):
        self.acc = self.vel * PLAYER_FRICTION
        self.input()
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.center = self.pos
        if self.rect.x > WIDTH:
            print("I'm off the right screen...")
        if self.rect.x < 0:
            print("I'm off the left screen...")
        if self.rect.y < 0:
            print("I'm off the top screen...")
        if self.rect.y > HEIGHT:
            print("I'm off the bottom screen...")

class Mob(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((50,50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.cofric = 0.1
        self.canjump = False
    def behavior(self):
        if self.rect.x < 0:
            self.vel.x *= -1
            self.pos.x += self.vel.x
        if self.rect.y < 0:
            self.vel.y *= -1
            self.pos.y += self.vel.y
        if self.rect.x > WIDTH:
            self.vel.x *= -1  
            self.pos.x += self.vel.x
        if self.rect.y > HEIGHT:
            self.vel.y *= -1
            self.pos.y += self.vel.y
    def update(self):
        self.behavior()
        self.pos += self.vel
        self.rect.center = self.pos
        