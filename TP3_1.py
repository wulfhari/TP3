#! /usr/bin/env python
# -*- coding:Utf8 -*-

"""
@file: TP3_1.py ------------------------------- NE PAS MODIFIER LE NOM DU FICHIER !
@author:  SIMON TOLSZCZUK-LECLERC    111 087 145

Module fournissant les fonctions suivantes :
    - Appartenance
    - Intersection
    - Différence
    - Ajout

Il fournit également les tests aux fonction suivantes : 
    - Test de la cardinalité
    - Test de l’union
    - Test de la différence symétrique
    - Test du retrait
"""

list_1 = ["a","b","t","allo","stop","clair","Quebec",2,3,54,7,5.4,6.7,9.8]
list_2 = ["a","e","f","123","go","clair","Quebec",1,4,78,7,5.3,6.7,9.8]

def appartient(e, s):
    """Commentaires ?"""
    for i in range(len(s)):
        if e == s[i]:
            return True
    else:
        return False


def intersection(s1, s2):
    """Commentaires ?"""
    s3 = []
    for i in range(len(s1)):
        for k in range((s2)):
            if s1[i] == s2[k]:
                s3.append(s1[i])
            
    return s3
            

def difference(s1, s2):
    """Commentaires ?"""
    s3 = []
    for i in range(len(s1)):
        for k in range(len(s2)):
            if s1[i] == s2[k]:
                break
            else:
                s3.append(s1[i])
    return s3

def ajout(e, s):
    """Commentaires ?"""
    return s.append(e)


"""
from TP3_2 import cardinalite, union, diff_symetrique, retrait


def test_cardinalite():
    s = ["a","b","t","allo","stop","clair","Quebec",2,3,54,7,5.4,6.7,9.8]
    assert( 14 == cardinalite(s))

def test_union():
    s1 = ["a","b","t","allo","stop","clair","Quebec",2,3,54,7,5.4,6.7,9.8]
    s2 = ["a","e","f","123","go","clair","Quebec",1,4,78,7,5.3,6.7,9.8]
    s3 = ["a","b","e","f","t","123","go","allo","stop","clair","Quebec",1,4,78,5.3,2,3,54,7,5.4,6.7,9.8]
    assert(s3 == union(s1, s2))

def test_diff_symetrique():
    s1 = ["a","b","t","allo","stop","clair","Quebec",2,3,54,7,5.4,6.7,9.8]
    s2 = ["a","e","f","123","go","clair","Quebec",1,4,78,7,5.3,6.7,9.8]
    diff_symetrique(s1, s2)
    #assert all(a[key] > b[key] for key in b)

def test_retrait():
    e = "clair"
    s = ["a","e","f","123","go","clair","Quebec",1,4,78,7,5.3,6.7,9.8]
    retrait(e, s)


if __name__ == "__main__":
    test_cardinalite()
    test_union()
    test_diff_symetrique()
    test_retrait()
"""    
    
s1 = ["a","b","t","allo","stop","clair","Quebec",2,3,54,7,5.4,6.7,9.8]
s2 = ["a","e","f","123","go","clair","Quebec",1,4,78,7,5.3,6.7,9.8]    

print(intersection(s1,s2))

