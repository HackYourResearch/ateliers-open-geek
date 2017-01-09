# Atelier #09 :  Graphes et réseaux, principes de base

*Internet, réseaux sociaux, cartes routières, infrastructures réseau, cartographies... les graphes sont partout autour de nous, et font partie de notre quotidien. Mais c’est quoi, un graphe ?* 

*Avec ce cours, découvrez les bases de la théorie des graphes et ses applications !*


## Résumé de la séance et de ses objectifs :

Dans cet atelier 09 Open Geek, nous ferons **une introduction à la théorie des graphes** : nous présenterons les **notions de base**, avec des exemples tirés de différents domaines, et nous verrons ensemble comment réaliser des **opérations simples** sur ces graphes.

Pour les participants les plus avancés, plusieurs **exercices** sur différents thématiques liées aux graphes sont disponibles tout au long du cours.

### Pré-requis :

- venir avec un ordinateur ;
- installer Python sur cet ordinateur ;
- avoir les connaissances de base en programmation pour pouvoir mieux suivre l'atelier

### Infos pratiques :

- Mardi 10 janvier de 19h30 à 22h30 à La Paillasse (Paris)

- Formateurs : Constance de Quatrebarbes & Romain André-Lovichi

## Points abordés lors de l'atelier


### 1. Motivations


Derrière le terme "théorie des graphes", on trouve en fait tout un tas de situations qui font partie de notre quotidien.

- Cartes routières

![Cartes routières](https://github.com/HackYourPhd/ateliers-open-geek/blob/master/Atelier_09/images/graphe_routes.jpg)

- Interactions sociales 

![Interactions sociales](https://github.com/HackYourPhd/ateliers-open-geek/blob/master/Atelier_09/images/graphe_social.jpg)

- Internet et communication

![Algorithme PageRank](https://github.com/HackYourPhd/ateliers-open-geek/blob/master/Atelier_09/images/graphes-internet.png)

*Image : Felipe Micaroni Lalli, CC-By-SA*

- Réseaux domestiques

![Réseaux domestiques](https://github.com/HackYourPhd/ateliers-open-geek/blob/master/Atelier_09/images/graphe_electricite.jpg)

Avec la séance d'aujourd'hui, nous allons essayer de voir comment la théorie des graphes permet de modéliser et d'étudier ces différentes situations.


### 2. Un peu de théorie

#### Définition peu, voire pas du tout formelle

En observant les différentes situations précédentes, on peut commencer à esquisser une première définition informelle d'un graphe :

- des points
  - souvent associés à un libellé
  - parfois coloriés
  
- des lignes
  - pas toujours droites
  - avec parfois un libellé

TODO Image

#### Définition formelle

Un graphe est défini par deux ensembles

- Un ensemble de sommets ***X*** 
Exemple : *X = {x, y, z}*

- Un ensemble d'arêtes ***E***, constitué de paires d'éléments de ***X***
Exemple : *E = {(x,y), (x, z)}

TODO Image


#### Voisins

Les sommets reliés par une arête sont appelés les extrémités de cette arête

Deux sommets reliés par une arête sont dits voisins ou adjacents

Le voisinage d'un sommet est l'ensemble de ses voisins

TODO Image

#### Graphes orientés / graphes non orientés

On pourrait mettre des flèches sur nos arêtes, pour n'autoriser les trajets que dans un seul sens.
Ex : routes à sens uniques

Pour commencer, on restera dans le cas simple des graphes sans flèches, appelés graphes non orientés.

TODO Image


#### Graphes simples / graphes complexes

On pourrait aussi envisager :
Plus d'une arête entre deux sommets
Des arêtes partant et arrivant sur le même sommet

Mais on peut toujours se ramener à un graphe ne présentant pas ces types d'arêtes

Donc on ne travaillera qu'avec des graphes simples, c'est-à-dire où ces configurations n'apparaissent pas

TODO Image


### 3. Votre premier graphe en Python

Bibliothèques utilisées : numpy, networkx, matplotlib

Premiers exo
 

### 4. Notions de voisinages

#### Voisins et degrés

Le degré d'un sommet est : 
le nombre d'arêtes partant de ce sommet
le nombre de voisins de ce sommet
la taille du voisinage de ce sommet

Un sommet de degré 0 (sans aucun voisin) est appelé sommet isolé.

TODO Image


#### Somme des degrés dans un graphe

La somme des degrés dans un graphe simple est paire (exemple des 3 matchs pour 5)

Représentations possibles : matrices et listes de voisinage

Exo
 

### 5. Composantes connexes

Intuitions

Définition "formelle"

Exo
 

### 6. Parcours dans un graphe

Qu'est-ce qu'un parcours ?

Arbres et cycles

Plus court chemin dans un graphe : parcours en largeur

Exo
 
 
### 7. Graphe étiqueté

Pourquoi des étiquettes ? (exemple d'une carte routière)

Plus court chemin (avec des exemples)

Algorithme de Dijsktra

Exo


### 8. Problèmes célèbres sur les graphes (avec des exos à chaque fois)
Graphes planaires
Parcours eulériens (fermés, ouverts)
Coloration


### 9. Des questions : que faire ?

- découvrez des tutoriels avancés (cf. ressources à la fin de ce billet)
- suivez d'autres formations dans vote université ou avec HYPhD ;).

### 10. Ressources supplémentaires

Fiche réalisée par Constance de Quatrebarbes et Romain André-Lovichi (licence CC-BY-SA)
