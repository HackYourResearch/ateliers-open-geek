# OpenGeek Apprentissage Automatique

Cet atelier s'agit d'une discussion autour des thématiques ci-dessous, à partir des points et liens présentés.

## Quelques liens
[Comment resoudre un probleme de data science](https://openclassrooms.com/courses/initiez-vous-au-machine-learning/comment-resoudre-un-probleme-de-data-science)

[Qu'est-ce que le machine learning](https://openclassrooms.com/courses/initiez-vous-au-machine-learning/qu-est-ce-que-le-machine-learning)

[Introduction au machine learning](https://cvernade.wp.imt.fr/teaching/introduction-au-machine-learning/)

[A tour of machine learning algorithms](http://machinelearningmastery.com/a-tour-of-machine-learning-algorithms/)

[Machine Learning theory an introductory primer](https://www.toptal.com/machine-learning/machine-learning-theory-an-introductory-primer)

[Scikit-Learn Tutorial](http://scikit-learn.org/stable/tutorial/basic/tutorial.html)

## Introduction
Historique

Concepts: généralisation, abstraction, régularisation, réduction

## Démarche

Point de départ de l'actualité: grosses donnés, grosses ordinateurs, itérer.

Discuter des exemples concrets. Pour chaque exemple, à quel intuition mathématique très simple ça correspond le plus.

Exercices de intelligence collectif: on vote pour comment classifier les problèmes.

Jouer avec le meta-jeu: nous votons pour classifier les exemples d'apprentissage automatique ; comparer avec le score individuel.

## Identifier le problème

###Non supervisé
Trouver des régularités dans un ensemble à partir d'un modèle pré-établi.

Canard X castor X ornithorynque, équipes de football.

![](http://cubiclebot.com/wp-content/uploads/2010/06/tumblr_l3uy4q3d631qzpwi0o1_.jpg)

En géneral, toute méthode de décomposition ou réduction de matrices.

Classification par proximité, clusterisation, réduction de dimensions, compression, PCA (analyse de composant principal).

On peut penser qui ça correspond à une mesure, un critère, défini implicitement ou explicitement.

### Supervised classification
Quand la réponse est discrète

Arbre de décision, ...

### Supervised regression
Quand la réponse est continue

Interpolation, ...

### Ingénierie de caracteristiques ("feature extraction")

''padding'': gérer les bords

normalisation: gérer le niveau, la moyenne des donnés

augmentation: transformer les donnés pour agrandir les ensembles, translations, zooms, inversions

faire attention à l'ingénierie de tous les ensembles: d'apprentissage, de validation, de test

### Evaluation

Ensembles:
* ensemble d'apprentissage
* ensemble de validation
* ensemble de test

Notions:
* Donné
* Modèle
* Score
* Loss
* Weights
* Accuracy

Sensitivity vs specificity

Overfitting

Topiques:

* Réseau de neurones
* Convolutional networks
* Transfer learning
* Reinforcement Learning
* Evolution Strategies <https://arxiv.org/abs/1703.03864>

Il faut comprendre comment construire l'architecture du réseau... et [ça se corse](https://culurciello.github.io/tech/2016/06/04/nets.html)!


### Passons à la pratique

Reconnaitre des numéros écrits à la main
[Digits Classification](http://scikit-learn.org/stable/auto_examples/classification/plot_digits_classification.html)

[MNIST filters](http://scikit-learn.org/stable/auto_examples/neural_networks/plot_mnist_filters.html)

[MNIST MLP](https://github.com/fchollet/keras/blob/master/examples/mnist_mlp.py)

Distinguer entre des chats et des chiens
[Donnés](https://www.kaggle.com/c/dogs-vs-cats-redux-kernels-edition)
[Tutorial with Keras](https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html)
