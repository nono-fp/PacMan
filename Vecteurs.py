# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 11:49:35 2025

@author: n.faivrepierret
"""

import math

#tutoriel : tresh moi :sueil
#tutoriel :__eq__ moi : __egalite__
#tutoriel asTuple (self) moi : convertir_tuple

#Explications : les fonctions avec __exemple__ c'est parce qu'on redéfinit des opérations de base

class Vecteur2D:
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.seuil= 0.000001
    
    #additionne deux vecteurs
    def __add__(self,vec):
        return Vecteur2D(self.x + vec.x, self.y + vec.y)
    
    #soustrait deux vecteurs
    def __sub__(self, vec):
        return Vecteur2D(self.x- vec.x, self.y - vec.y)
    
    #renvoie l'opposé d'un vecteur
    def __neg__(self):
        return Vecteur2D(-self.x , -self.y)
    
    #multiplie chaque composante du vecteur par un scalaire
    def __mul__(self, scalaire):
        return Vecteur2D(self.x * scalaire, self.y * scalaire)
    
    #divise chaque composante du vecteur par un scalaire
    def __div__(self,scalaire):
        if scalaire != 0:
            return Vecteur2D(self.x / float(scalaire), self.y / float(scalaire))
        return None
    
    
    def __truediv__(self,scalaire):
        return self.__div__(scalaire)
    
    def __egalite__(self, other):
        #abs renvoie la valeur absolue d'un nombre
        if abs(self.x - other.x) < self.seuil :
            if abs(self.y - other.y) < self.seuil:
                return True
        return False
    
    ''' méthode magnitude (longueur) : utilise racine carrée
        methode  magnitudeSquared : ne nécessite pas de racine carrée'''
    
    def magnitudeSquared (self):
        return self.x ** 2 + self.y**2
    
    def magnitude(self):
        return math.sqrt(self.magnitudeSquared())
    
    # copie des vecteurs pour les modifier sans toucher aux vecteurs de base
    def __copy__(self):
        return Vecteur2D (self.x , self.y)
    
    #convertir le vecteur en tuple
    def convertir_tuple (self):
        return (self.x, self.y)
    
    
    #convertir les coordonnées en entiers et mettre le tout sous forme de tuple
    def asInt(self):
        return (int(self.x), int(self.y))

    def __str__(self):
        return "<"+str(self.x)+", "+str(self.y)+">"


    
