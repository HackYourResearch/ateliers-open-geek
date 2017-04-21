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

def order_graph(g):
    '''calculer la somme des degrés d'un graphe'''
    # Niveau 1: en utilisant un compteur
    # compter le nombre de connexion pour chacun des noeuds
    cpt = 0
    for node in g.nodes():
        cpt += g.degree(node)
    print("Le graphe est d'ordre", cpt)
    # Niveau 3: en utilisant sum(list) dans une liste compréhension
    #return (sum([g.degree(node) for node in g.nodes()]))
    return cpt

if __name__ == "__main__":
    g = build_graph_from_csv()
    order_graph(g)
