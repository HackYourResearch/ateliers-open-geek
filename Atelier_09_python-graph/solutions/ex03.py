#!usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import csv

def build_graph(csv_f_name):
    #instancier le graph
    g = nx.Graph()
    with open(csv_f_name) as f:
        reader = csv.reader(f, delimiter=",")
        for i,line in enumerate(reader):
            if i == 0:
                #on passe la première ligne
                pass
            else:
                #ajouter chaque arête du graph ajoutera les sommets
                g.add_edge(line[0], line[1], weight=line[2])
    nx.draw(g, with_labels=True)
    plt.savefig(csv_f_name.replace(".csv",".png")) # save as png
    plt.show() # afficher
    return g

if __name__ == "__main__":
    g = build_graph("miserables.csv")
