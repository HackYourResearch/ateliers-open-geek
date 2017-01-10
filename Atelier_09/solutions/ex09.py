#!usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import csv

def sont_voisins(g, name1, name2):
    '''est_voisin si le sommet 1 est relié au sommet 2'''
    for edge in g.edges(name1):
        print(edge)
        #niveau 2: appartient à la liste
        if name2 in edge:
            print("%s et %s sont bien voisins" %(name1, name2))

        #niveau 1: test d'égalité
        #if name2 == edge[1]:
            #print("%s et %s sont bien voisins" %(name1, name2))
            #break
            return True
    return False
    #niveau3
    #function presente dans networkx testée avec Booléen
    #return bool(name2 in g.neighbors(name1))

if __name__ == "__main__":
    g = build_graph_from_csv()
    #exercice 7
    sont_voisins(g, "Javert", "Mme.Thenardier")
