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
                #on ne prend que le nom1, nom2, et le nombre d'occ en poids (facultatif)
                g.add_edge(line[0], line[1], weight=line[2])
    return g


def sociability_degree(g, nom):
    '''function qui renoie le nombre de liens d'un sommets'''
    #niveau 1: somme des liens qui contiennent le nom
    #print(len(g.edges(name)))
    #niveau: 2 fonction toute faite de networkx
    print("%s a %i relations" %(nom, g.degree(nom)))
    return(g.degree(nom))

if __name__ == "__main__":
    g = build_graph_from_csv()
    #exercice 4
    print(sociability_degree(g, "Javert"))
