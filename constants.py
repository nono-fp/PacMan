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
STOP = 0
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4
PORTAL = 3 #nbr aléatoire pas d'importance
PACMAN = 0
PELLET  = 1
POWERPELLET = 2
GHOST = 3
SCATTER = 0 #dispersion
CHASE = 1 #poursuite
FREIGHT = 2 #fret
SPAWN = 3 # apparition
""""

X" : espace vide

"+": Nœud

".": Chemin vertical / horizontal

"""
"""
mode dispersion : 7 secondes
mode poursuite : 20 secondes
"""
