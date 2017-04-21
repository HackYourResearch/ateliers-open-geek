#!usr/bin/python3
#importer les libraires
#pour afficher
import matplotlib.pyplot as plt
#pour le calcul
import numpy as np
#pour le réseau
import networkx as nx

#instancier le graph
g = nx.Graph()
#ajouter un noeud
#g.add_node("paul")
#ajouter une liste de noeud
g.add_nodes_from(["Turgot", "Hume", "Diderot", "D'Alembert", "Rousseau"])
#ajouter un lien
#g.add_edge(["Diderot", "D'Alembert"])
#ajouter une liste de liens
g.add_edges_from([("Diderot", "D'Alembert"), ("Turgot", "Hume"),("Rousseau", "D'Alembert"), ("D'Alembert", "Hume"),("Rousseau", "Diderot")])
# dessiner le graph en affichant les labels des noeuds
nx.draw(g, with_labels=True)
# enregistrer l'image comme png
plt.savefig("graphe_philosophes.png") # save as png
# afficher
plt.show()
