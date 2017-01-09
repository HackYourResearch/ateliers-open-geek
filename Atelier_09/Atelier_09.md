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

- des **points**
  - souvent associés à un libellé
  - parfois coloriés
  
- des **lignes**
  - pas toujours droites
  - avec parfois un libellé

![Définition informelle d'un graphe : exemple](https://github.com/HackYourPhd/ateliers-open-geek/blob/master/Atelier_09/images/graphe-0.jpg)

#### Définition formelle

Un graphe est défini par deux ensembles

- Un ensemble de **sommets** ***X*** 
Exemple : *X = {x, y, z}*

- Un ensemble d'**arêtes** ***E***, constitué de paires d'éléments de ***X***
Exemple : *E = {(x,y), (x, z)}

![Définition formelle d'un graphe : exemple](https://github.com/HackYourPhd/ateliers-open-geek/blob/master/Atelier_09/images/graphe-1.jpg)


#### Voisins

Les sommets reliés par une arête sont appelés les **extrémités** de cette arête

Deux sommets reliés par une arête sont dits **voisins** ou **adjacents**

Le **voisinage** d'un sommet est l'ensemble de ses voisins


#### Graphes orientés / graphes non orientés

On pourrait mettre des flèches sur nos arêtes, pour n'autoriser les trajets que dans un seul sens (comme par exemple dans le cas d'une route à à sens unique). On parle alors de **graphes orientés**.

![Graphe orienté](https://github.com/HackYourPhd/ateliers-open-geek/blob/master/Atelier_09/images/graphe-oriente-1.jpg)

Dans un premier temps, on restera cependant dans le cas simple des graphes "sans flèches", appelés **graphes non orientés**.

![Graphe non orienté](https://github.com/HackYourPhd/ateliers-open-geek/blob/master/Atelier_09/images/graphe-oriente-0.jpg)


#### Graphes simples / graphes complexes

On pourrait aussi envisager des situations un peu plus complexes :

- Plus d'une arête entre deux sommets
- Des arêtes partant et arrivant sur le même sommet

![Graphe complexe](https://github.com/HackYourPhd/ateliers-open-geek/blob/master/Atelier_09/images/graphe-simple-0.jpg)

Cependant, on peut généralement se ramener à un graphe ne présentant pas ces types d'arêtes :

![Graphe simple](https://github.com/HackYourPhd/ateliers-open-geek/blob/master/Atelier_09/images/graphe-simple-1.jpg)

Dans le cadre de cet atelier, on ne travaillera donc qu'avec des **graphes simples**, c'est-à-dire où ces configurations n'apparaissent pas.


### 3. Votre premier graphe en Python

Bibliothèques utilisées : numpy, networkx, matplotlib

EXO : Importer les bibliothèques (et vérifier que ça marche)

Premiers exo

EXO : Recopier un bout de code pour afficher un graphe

EXO : Créer un graphe à partir d'un court énoncé, qui liste les sommets (ex : personnages), et les liens entre eux (ex : X connait Y, etc.)


### 4. Notions de voisinages

#### Voisins et degrés

Le degré d'un sommet est : 
le nombre d'arêtes partant de ce sommet
le nombre de voisins de ce sommet
la taille du voisinage de ce sommet

Un sommet de degré 0 (sans aucun voisin) est appelé sommet isolé.

TODO Image

EXO : Afficher le degré d'un sommet

EXO : Afficher la liste des voisins d'un sommet


#### Somme des degrés dans un graphe

TODO : Image echecs ?

La somme des degrés dans un graphe simple est paire (exemple des 3 matchs pour 5)

Représentations possibles : matrices et listes de voisinage

EXO : Calculer la somme des degré des sommets dans un graphe


### 5. Composantes connexes

Intuitions

Définition "formelle"

EXO : Tester si deux sommets sont voisisn

EXO : Tester si deux sommets appartiennent à la même composantes connexe (avec peut-être des indications/indices sur comment le faire ?)
 

### 6. Parcours dans un graphe

Qu'est-ce qu'un parcours ?

TODO Image

Arbres et cycles

TODO Images

Plus court chemin dans un graphe : parcours en largeur

EXO : Lister tous les sommets parcourus (parcours en largeur)

EXO : Lister tous les sommets parcours (parcours en profondeur)
 
 
### 7. Graphe étiqueté

Pourquoi des étiquettes ? (exemple d'une carte routière)

Plus court chemin (avec des exemples)

Algorithme de Dijsktra

EXO : Calcul du plus court chemin dans un graphe étiquetté


### 8. Problèmes célèbres sur les graphes (avec des exos à chaque fois)

Graphes planaires

Parcours eulériens (fermés, ouverts)

Coloration


### 9. Quelques exemples concrets de l'utilisation des graphes sur des sujets de recherche



### 10. Des questions : que faire ?

- découvrez des tutoriels avancés (cf. ressources à la fin de ce billet)
- suivez d'autres formations dans vote université ou avec HYPhD ;).


### 11. Ressources supplémentaires

Fiche réalisée par Constance de Quatrebarbes et Romain André-Lovichi (licence CC-BY-SA)
