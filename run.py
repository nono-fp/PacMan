import pygame
import sys
from pygame.locals import *
from constants import *
from pacman import Pacman
from nodes import NodeGroup
from pellets import PelletGroup
from ghosts import GhostGroup

class GameController(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREENSIZE, 0, 32)
        self.background = None
        self.clock = pygame.time.Clock()

    def setBackground(self):
        self.background = pygame.surface.Surface(SCREENSIZE).convert()
        self.background.fill(BLACK)

    def startGame(self):
     self.setBackground ()
     self.nodes = NodeGroup ( "maze1.txt" )
     self.nodes.setPortalPair ((7,17), (34,17))
     homekey = self.nodes.createHomeNodes(17.5, 10)
     self.nodes.connectHomeNodes(homekey, (18,10), LEFT)
     self.nodes.connectHomeNodes(homekey, (21,10), RIGHT)
     self.pacman = Pacman(self.nodes.getNodeFromTiles(21, 22))
     self.pellets = PelletGroup("maze1.txt")
     self.ghosts = GhostGroup(self.nodes.getStartTempNode(), self.pacman)
     self.ghosts.blinky.setStartNode(self.nodes.getNodeFromTiles(2+17.5, 0+10))
     self.ghosts.pinky.setStartNode(self.nodes.getNodeFromTiles(2+17.5, 3+10))
     self.ghosts.inky.setStartNode(self.nodes.getNodeFromTiles(0+17.5, 3+10))
     self.ghosts.clyde.setStartNode(self.nodes.getNodeFromTiles(4+17.5, 3+10))
     self.ghosts.setSpawnNode(self.nodes.getNodeFromTiles(2+17.5, 3+10))

    def update(self):
        dt = self.clock.tick(30) / 1000.0
        self.pacman.update(dt)
        self.ghosts.update(dt)
        self.pellets.update(dt)
        self.checkPelletEvents()
        self.checkGhostEvents()
        self.checkEvents()
        self.render()

    def checkGhostEvents(self):
        for ghost in self.ghosts:
            if self.pacman.collideGhost(ghost):
                if ghost.mode.current is FREIGHT:
                    ghost.startSpawn()
               
    def checkEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()
                    
    def checkPelletEvents(self):
        pellet = self.pacman.eatPellets(self.pellets.pelletList)
        if pellet:
            self.pellets.numEaten += 1
            self.pellets.pelletList.remove(pellet) 
            if pellet.name == POWERPELLET :
                self.ghosts.startFreight()
            
    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.nodes.render(self.screen)
        self.pellets.render(self.screen)
        self.pacman.render(self.screen)
        self.ghosts.render(self.screen)
        pygame.display.update()

    
if __name__ == "__main__":
    game = GameController()
    game.startGame()
    while True:
        game.update()
    game.quit()
