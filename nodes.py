# -*- coding: utf-8 -*-
#neighbor : voisins
#nodeList : nodeListe
import pygame as py
from constants import *
from Vecteurs import Vecteur2D

class Node(object):
    
    def __init__(self,x,y):
        self.position = Vecteur2D(x,y)
        self.voisins = {UP : None, DOWN : None, LEFT : None, RIGHT : None}
        
    def render(self,screen):
        for n in self.voisins.keys():
            if self.voisins[n] is not None:
                ligne_start = self.position.convertir_tuple()
                ligne_end = self.voisins[n].position.convertir_tuple()
                py.draw.line(screen,WHITE,ligne_start,ligne_end,4)
                py.draw.circle(screen,RED,self.position.asInt(),12)
                
                
class NodeGroup(object):
    
    def __init__(self):
        self.nodeListe =[]
        
    def setupTestNodes(self):
        nodeA = Node(80 ,80)
        nodeB = Node(160, 80)
        nodeC = Node(80, 160)
        nodeD = Node(160, 160)
        nodeE = Node(208, 160)
        nodeF = Node(80, 320)
        nodeG = Node(208, 320)
        nodeA.voisins[RIGHT] = nodeB
        nodeA.voisins[DOWN] = nodeC
        nodeB.voisins[LEFT] = nodeA
        nodeB.voisins[DOWN] = nodeD
        nodeC.voisins[UP] = nodeA
        nodeC.voisins[RIGHT] = nodeD
        nodeC.voisins[DOWN] = nodeF
        nodeD.voisins[UP] = nodeB
        nodeD.voisins[LEFT] = nodeC
        nodeD.voisins[RIGHT] = nodeE
        nodeE.voisins[LEFT] = nodeD
        nodeE.voisins[DOWN] = nodeG
        nodeF.voisins[UP] = nodeC
        nodeF.voisins[RIGHT] = nodeG
        nodeG.voisins[UP] = nodeE
        nodeG.voisins[LEFT] = nodeF
        self.nodeListe = [nodeA, nodeB, nodeC, nodeD, nodeE, nodeF, nodeG]

    def render(self, screen):
        for node in self.nodeListe:
            node.render(screen)
