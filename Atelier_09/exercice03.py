#!usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import csv

#instancier le graph
g = nx.Graph()
with open("miserables.csv") as f:
    reader = csv.reader(f, delimiter=",")
    for i,line in enumerate(reader):
        if i == 0:
            #on passe la première ligne
            pass
        else:
            #print(line)
            g.add_edge(line[0], line[1], weight=line[2])

nx.draw(g, with_labels=True)
plt.savefig("miserables.png") # save as png
plt.show() # afficher
