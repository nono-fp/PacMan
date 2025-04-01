# -*- coding: utf-8 -*-

import pygame as py
import sys
from pygame.locals import *
from constants import *
from pacman import Pacman
from nodes import NodeGroup

class GameController (object):
    
    def __init__(self):
        py.init()
        # créer fenetre de jeu + 0 : pas d'option spéciale, 32 : nbr de bits pour la surface
        self.screen =py.display.set_mode(DIMENSION_FENETRE, 0, 32) 
        self.background = None
        self.running = True
        self.clock = py.time.Clock()

    def setBackground(self):
        self.background = py.surface.Surface(DIMENSION_FENETRE).convert()
        self.background.fill(BLACK)
        
    def startGame(self):
        self.setBackground ()
        self.nodes = NodeGroup()
        self.nodes.setupTestNodes()
        self.pacman = Pacman(self.nodes.nodeListe[0])
        
    def update (self):
        dt = self.clock.tick(30)/1000.0 # renvoie le temps écoulé en millis depuis dernier appel
        self.pacman.update(dt)
        self.checkEvents() # Vérifie le moment où on quitte le jeu avec X
        self.render () # méthode pour afficher les images à l'écran
        
    def checkEvents (self):
        for event in py.event.get():
            if event.type == QUIT :
                self.running = False
                
    def render(self):
        self.screen.blit(self.background, (0,0))
        self.nodes.render(self.screen)
        self.pacman.render(self.screen)
        py.display.update()
        
        
if __name__ == "__main__":
    game = GameController ()
    game.startGame()
    while game.running :
        game.update()
    
py.quit()
sys.exit()
