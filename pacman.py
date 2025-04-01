# -*- coding: utf-8 -*-
import pygame as py
from pygame.locals import *
from constants import *
from Vecteurs import Vecteur2D


class Pacman(object):
    
    def __init__(self):
        self.name = PACMAN
        #self.position = Vecteur2D(LARGEUR_FENETRE // 2, HAUTEUR_FENETRE // 2)
        self.directions = {STOP:Vecteur2D(),UP:Vecteur2D(0,-1), DOWN:Vecteur2D(0,1), RIGHT:Vecteur2D(1,0), LEFT : Vecteur2D(-1,0)}
        self.direction = STOP
        self.speed = 100 * LARGEUR_DE_TUILE /20
        self.radius = 10
        self.color = YELLOW
        self.node = node
        self.setPosition()
        
    def setPosition(self):
        self.position = self.node.position.copy()
        
    def update(self,dt):
        #self.position += self.directions[self.direction]*self.speed*dt
        direction = self.getValidKey()
        self.direction = direction
        self.node = self.getNewTarget(direction)
        self.setPosition()
        
    def validDirection(self, direction):
        if direction is not STOP:
            if self.node.voisins[direction] is not None:
                return True
        return False

    def getNewTarget(self, direction):
        if self.validDirection(direction):
            return self.node.voisins[direction]
        return self.node
        
    def getValidKey(self):
        key_pressed = py.key.get_pressed()
        if key_pressed[K_UP]:
            return UP
        if key_pressed[K_DOWN]:
            return DOWN
        if key_pressed[K_LEFT]:
            return LEFT
        if key_pressed[K_RIGHT]:
            return RIGHT
        return STOP
    
    def render(self, screen):
        p =self.position.asInt()
        py.draw.circle(screen,self.color, p , self.radius)
