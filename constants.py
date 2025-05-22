# -*- coding: utf-8 -*-


TILEWIDTH = 20
TILEHEIGHT = 20
NCOLS = 40 # NCOLS
NROWS = 30 # NROWS
SCREENWIDTH =  NCOLS * TILEWIDTH
SCREENHEIGHT = NROWS * TILEHEIGHT
SCREENSIZE = (SCREENWIDTH, SCREENHEIGHT)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255,255,0)
RED = (255, 0,0)
PINK = (255, 100, 150)
TEAL = (100, 255, 255)
ORANGE = (230, 190, 40)

STOP = 0
UP = 1
DOWN = -1
LEFT = 2
RIGHT = -2

PORTAL = 3 #nbr aléatoire pas d'importance
PACMAN = 0
PELLET  = 1
POWERPELLET = 2
GHOST = 3


SCATTER = 0 #dispersion
CHASE = 1 #poursuite
FREIGHT = 2 #fret
SPAWN = 3 # apparition


#nom des fantômes
BLINKY = 4
PINKY = 5
INKY = 6
CLYDE = 7


""""

X" : espace vide

"+": Nœud

".": Chemin vertical / horizontal

"""
"""
mode dispersion : 7 secondes
mode poursuite : 20 secondes
"""
