#! /usr/bin/env python
# -*- coding:Utf8 -*-

"""
@file: TP3_2.py ------------------------------- NE PAS MODIFIER LE NOM DU FICHIER !
@author:  C. Besse

Module fournissant les fonctions suivantes :
    - Cardinalité
    - Union
    - Différence symétrique
    - Retrait

Il fournit également les tests aux fonction suivantes : 
    - Test de l’appartenance
    - Test de l’intersection
    - Test de la différence
    - Test de l’ajout
"""

def cardinalite(s):
    """Commentaires ?"""
    return len(s)

def union(s1, s2):
    """Commentaires ?"""
    united = []
    for i in s1:
        united.append(i)
    for j in s2:
        united.append(j)
    for u in united:
        for k in united:
            if u == k:
                del(united[k])
            
    return united

def diff_symetrique(s1, s2):
    """Commentaires ?"""
    from TP3_1 import intersection
    uni = union(s1,s2)
    inter = intersection(s1,s2)
    return uni - inter

def retrait(e, s):
    """Commentaires ?"""
    for i in range(0,len(s)):
        if i == e:
            del(s[i])

from TP3_1 import ajout, appartient, difference, intersection

def test_appartient():
    e = "bla"
    s = "bla"
    appartient(e, s)

def test_intersection():
    s1 = "bla"
    s2 = "bla"
    intersection(s1, s2)

def test_difference():
    s1 = "bla"
    s2 = "bla"
    difference(s1, s2)

def test_ajout():
    e = "bla"
    s = "bla"
    ajout(e, s)

if __name__ == "__main__":
    test_appartient()
    test_intersection()
    test_difference()
    test_ajout()
