#!usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import csv

def build_graph_from_csv(f_name="miserables.csv"):
#instancier le graph
    g = nx.Graph()
    with open(f_name) as f:
        reader = csv.reader(f, delimiter=",")
        for i,line in enumerate(reader):
            if i == 0:
                #on passe la première ligne
                pass
            else:
                #print(line)
                #on ne prend que le nom1, nom2, et le nombre d'occ
                g.add_edge(line[0], line[1], weight=line[2])
    return g

#print(g.neighbors("Javert"))
def sociability_degree(g, nom):
    #somme des liens qui contiennent le nom
    #print(len(g.edges(name)))
    #fonction toute faite de networkx
    print("%s a %i relations" %(nom, g.degree(nom)))
    return(g.degree(nom))

def connexions(g, nom):
    #niveau 1: liens qui contiennent le nom
    return [n[1] for n in g.edges(name)]
    # #fonction toute faite de networkx
    # print("%s connait:" %nom)
    # for n in g.neighbors(nom):
    #     print("-", n)
    # return(g.neighbors(nom))

def order_graph(g):
    '''calculer la somme des degrés d'un graphe'''
    # Niveau 1 en utilisant un compteur
    cpt = 0
    for node in g.nodes():
        cpt += g.degree(node)
    print("somme = ", cpt)
    # Niveau 4 en utilisant sum(list) dans une liste compréhension
    #return (sum([g.degree(node) for node in g.nodes()]))
    return cpt

def est_voisin(g, name1, name2):
    '''est_voisin s'il est relié'''
    # Niveau1

    for edge in g.edges(name1):
        print(edge)
        #appartient à la liste
        if name2 in edge:
            print("%s et %s sont bien voisins" %(name1, name2))
        # test d'égalité
        #if name2 == edge[1]:
            break
            return True

    return False
    #niveau3
    #function presente dans networkx testée avec Booléen
    #return bool(name2 in g.neighbors(name1))

if __name__ == "__main__":
    g = build_graph_from_csv()
    #exercice 4
    # sociability_degree(g, "Javert")
    # sociability_degree(g, "Fantine")
    # sociability_degree(g, "Valjean")
    # #exercice 5
    # connexions(g, "Javert")
    # connexions(g, "Fantine")
    # connexions(g, "Valjean")
    #exercice6
    #order_graph(g)
    #exercice 7
    #print(est_voisin(g, "Javert","Mme.Thenardier"))
    
    #print(graphs)
