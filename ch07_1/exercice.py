#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math
from ch06_1 import exercice
from turtle import *

# TODO: Définissez vos fonction ici
def operation_ellipsoide(x = 2.8, y = 3.0, z = 2.6, massevol = 3.6):
    volume =  (4 / 3) * math.pi * x * y * z
    masse = massevol * volume
    return round(volume, 3), round(masse, 3)

lambda sentence: sorted(exercice.frequence(sentence), key = exercice.frequence(sentence).__getitem__[-1])
    
def dessin(angle, j = 0):
    color('green')
    setheading(90)
    a = 50
    for i in range(5):
        forward(a)
        left(angle)
        a -= 8
        j += 1
        if j == 85:
            return done()
    penup()
    goto(0, 0)
    pendown()
    if angle > 30:
        return dessin(angle - 75, j)
    return dessin(angle + 10, j)

def valide(seq):
    for lettre in seq:
        if lettre not in 'acgt':
            return False
    return True

def saisie(type):
    seq = input(f"Entrez une {type} d'ADN valide:")
    if valide(seq):
        return seq
    print(f"La chaine {type} n'est pas valide")
    return saisie(type)

def proportion(chaine, sequence):
    pourcentage = round(len(sequence) * chaine.count(sequence) / len(chaine), 2)
    return pourcentage

def verifi_adn():
    chaine = saisie('chaine')
    sequence = saisie('sequence')
    pourcentage = proportion(chaine, sequence)
    return f"Il y a {pourcentage * 100} % de {sequence}"

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    pass