#!usr/bin/python3
#importer les libraires
#pour afficher
import matplotlib.pyplot as plt
#pour le calcul
import numpy as np
#pour le réseau
import networkx as nx

g = nx.Graph()

g.add_nodes_from(["Ann", "Betty", "Charlotte", "Félicia", "Georgia", "Helen", "Edith"])
#Ann dit avoir rencontré Betty, Charlotte, Félicia et Georgia;
g.add_edges_from([("Ann", n) for n in ["Betty", "Charlotte", "Félicia", "Georgia"]])
#Betty dit avoir rencontré Ann, Charlotte, Edith, Félicia, et Helen ;
g.add_edges_from([("Betty", n) for n in ["Ann", "Charlotte", "Edith", "Félicia", "Helen"]])
#Charlotte dit avoir rencontré Ann, Betty et Edith ;
g.add_edges_from([("Charlotte", n) for n in ["Ann", "Betty", "Edith"]])
#Edith dit avoir rencontré Betty, Charlotte et Félicia;
g.add_edges_from([("Edith", n) for n in ["Betty", "Charlotte", "Félicia"]])
#Félicia dit avoir rencontré Ann, Betty, Edith et Helen;
g.add_edges_from([("Félicia", n) for n in ["Ann", "Betty", "Edith", "Helen"]])
#Georgia dit avoir rencontré Ann et Helen ;
g.add_edges_from([("Georgia", n) for n in ["Ann", "Helen"]])
#Helen dit avoir rencontré Betty, Félicia et Georgia.
g.add_edges_from([("Helen", n) for n in ["Betty", "Félicia", "Georgia"]])
nx.draw(g, with_labels=True)
# enregistrer l'image comme png
plt.savefig("barbe_bleue.png") # save as png
# afficher
plt.show()

# afficher le nombre de sommets
print(g.nodes())
#afficher le nombre de connexions
print(g.edges())
