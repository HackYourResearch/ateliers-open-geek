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


def get_connexions(g, nom):
    '''lister les relations entretenues par un sommet'''
    #niveau2: fonction toute faite de networkx
    print("%s connait:" %nom)
    for n in g.neighbors(nom):
        print("-", n)
    # return(g.neighbors(nom))
    #niveau 1: tous les sommets contenu dans les liens de ce sommet
    return [n[1] for n in g.edges(nom)]

if __name__ == "__main__":
    g = build_graph_from_csv()
    #exercice 5
    get_connexions(g, "Javert")
