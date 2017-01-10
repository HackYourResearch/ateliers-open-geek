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
                #on passe la premiere ligne
                pass
            else:
                #print(line)
                #on ne prend que le nom1, nom2, et le nombre d'occ en poids (facultatif)
                g.add_edge(line[0], line[1], weight=line[2])

    return g

def build_dict(g):
    '''transformer un graphe en un dictionnaire de listes'''
    graph = {}
    for node in g.nodes():
        #graph[node] = [n1 for n in g.edges(node)]
        #ou
        graph[node] = g.neighbors(node)
    print graph
    return graph

if __name__ == "__main__":
    g = build_graph_from_csv()
    print_graph(g)
