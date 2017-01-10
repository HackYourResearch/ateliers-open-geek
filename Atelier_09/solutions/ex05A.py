#!usr/bin/python3
#importer les libraires
#pour afficher
import matplotlib.pyplot as plt
#pour le calcul
import numpy as np
#pour le réseau
import networkx as nx
# pour choisir au hasard dans une liste
import random

g = nx.Graph()
joueurs = ["Joueur1", "Joueur2", "Joueur3", "Joueur4", "Joueur5"]
g.add_nodes_from(joueurs)
for j in joueurs:
    #on enlève le joueur des adversaire
    adversaires = [adv for adv in joueurs if adv != j]
    #choisir trois joueurs au hasard parmi les adversaires
    adversaires = random.sample(adversaires, 3)
    for adv in  adversaires:
        print("%s afrontera %s" %(j,adv))
        g.add_edge(j,adv)

nx.draw(g, with_labels=True)
# enregistrer l'image comme png
plt.savefig("chess.png") # save as png
