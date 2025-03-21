# -*- coding: utf-8 -*-
import pygame as py
from constants import *
from Vecteurs import Vecteur2D

class Nodes(object):
    
    def __init__(self,x,y):
        self.position = Vecteur2D(x,y)
        self.voisins = {UP : None, DOWN : None, LEFT : None, RIGHT : None}
        
    def render(self,screen):
        for n in self.voisins.keys():
            if self.voisins[n] is not None:
                ligne_start = self.position.asTuple()
                ligne_end = self.voisins[n].poisition.asTuple()
                py.draw.line(screen,WHITE,ligne_start,ligne_end,4)
                py.draw.circle(screen,RED,self.position.asInt(),12)