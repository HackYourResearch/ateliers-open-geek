# OpenGeek Aprentissage Automatique

## Quelques liens
https://openclassrooms.com/courses/initiez-vous-au-machine-learning/comment-resoudre-un-probleme-de-data-science
https://openclassrooms.com/courses/initiez-vous-au-machine-learning/qu-est-ce-que-le-machine-learning
https://cvernade.wp.imt.fr/teaching/introduction-au-machine-learning/
http://machinelearningmastery.com/a-tour-of-machine-learning-algorithms/
https://www.toptal.com/machine-learning/machine-learning-theory-an-introductory-primer
http://scikit-learn.org/stable/tutorial/basic/tutorial.html

## Introduction
Historique
Concepts: généralisation, abstraction, régularisation, réduction

## Démarche
point de depart:  grosses donnés, grosses ordinateurs, itérer
discuter des exemples concrêts
pour chaque example, à quel intuition mathematique très simple ça corréspond le plus:
exercices de intelligence collectif: on vote pour comment classifier les problemes
jouer avec le meta-jeu: nous votons pour classifier les examples ; comparer avec le score individuel

### Identifier le problème

Non supervisé
canard / beaver / platypus <http://cubiclebot.com/wp-content/uploads/2010/06/tumblr_l3uy4q3d631qzpwi0o1_.jpg>
équipes de foot, ...

En géneral, toute méthode de décomposition ou réduction de matrices
proximité / clusterisation, réduction de dimensions, compression, PCA (analyse de composant principal)

On peut penser qui ça correspond à une mesure / critère défini implicitement ou explicitement

Supervised classification
arbre de décision
Supervised regression
interpolation (connecter des points)

### Ingénierie de caracteristiques ("feature extraction")
padding
normalization
augmentation
faire attention à tous les ensembles

### Evaluation
faire comprendre la notion d'ensemble d'apprentissage, de validation, et de test
data / score / loss / weights / accuracy
sensitivity vs specificity

### Passons à la pratique
- reconnaitre des numéros écrits à la main
    http://scikit-learn.org/stable/auto_examples/classification/plot_digits_classification.html
    http://scikit-learn.org/stable/auto_examples/neural_networks/plot_mnist_filters.html
    https://github.com/fchollet/keras/blob/master/examples/mnist_mlp.py
- distinguer entre des chats et des chiens
    https://www.kaggle.com/c/dogs-vs-cats-redux-kernels-edition
    https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html
- Convolutional networks
- Transfer learning
- Reinforcement Learning
- Evolution Strategies <https://arxiv.org/abs/1703.03864>

-  pour faire du réseau de neurones, il faut comprendre comment construir l'architecture du réseau
- ...et ça se corse! https://culurciello.github.io/tech/2016/06/04/nets.html
