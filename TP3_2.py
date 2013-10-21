#! /usr/bin/env python
# -*- coding:Utf8 -*-

"""
@file: TP3_2.py ------------------------------- NE PAS MODIFIER LE NOM DU FICHIER !
@author:  Zoé Tolszczuk-Leclerc 908 178 188

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
        if j in united:
            pass
        else:
            united.append(j)
    return united

def diff_symetrique(s1, s2):
    from TP3_1 import intersection
    """Commentaires ?"""
    uni = union(s1,s2)
    inter = intersection(s1,s2)
    
    for i in inter:       
        uni.remove(i)        
    return uni

def retrait(e, s):
    """Commentaires ?"""
    for i in s:
        if i == e:
            del(s[s.index(i)])
    return s


from TP3_1 import ajout, appartient, difference, intersection

def test_appartient():
    e = "Quebec"
    s = ["a","b","t","allo","stop","clair","Quebec",2,3,54,7,5.4,6.7,9.8]
    assert(True == appartient(e, s))
   
def test_intersection():
    s1 = ["a","b","t","allo","stop","clair","Quebec",2,3,54,7,5.4,6.7,9.8]
    s2 = ["a","e","f","123","go","clair","Quebec",1,4,78,7,5.3,6.7,9.8]
    s3 = ["a", "clair", "Quebec", 7, 6.7, 9.8]
    for i in s1:
        for j in s2:
            if i ==j:
                assert(s3.count(i) ==1)
   

def test_difference():
    s1 = ["a","b","t","allo","stop","clair","Quebec",2,3,54,7,5.4,6.7,9.8]
    s2 = ["a","e","f","123","go","clair","Quebec",1,4,78,7,5.3,6.7,9.8]
    s3 = ["b","t","allo","stop",2,3,54,5.4]
    assert ( len(s3) == len(difference(s1, s2)))
    for i in s2:
        assert (s3.count(i) == 0)

def test_ajout():
    e = "Volga"
    s = ["a","b","t","allo","stop","clair","Quebec",2,3,54,7,5.4,6.7,9.8]
    s1 = ajout(e, s)
    assert(s1.count(e) == 1)

           
if __name__ == "__main__":
    test_appartient()
    test_intersection()
    test_difference()
    test_ajout()

