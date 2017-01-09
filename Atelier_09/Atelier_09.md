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

*Image : Felipe Micaroni Lalli, CC-BY-SA*

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


#### Représenter un graphe

Il est important de noter que cette définition ne fait référence à aucune coordonnée spatiale. Il existe donc de multiples représentations d’un même graphe.

Par exemple, les deux représentations ci-dessous correspondent au même graphe : 

![Différentes représentations d'un même graphe](https://github.com/HackYourPhd/ateliers-open-geek/blob/master/Atelier_09/images/representations.jpg)


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

Le **degré** d'un sommet est : 

- le nombre d'arêtes partant de ce sommet
- le nombre de voisins de ce sommet
- la taille du voisinage de ce sommet

Un sommet de degré 0 (sans aucun voisin) est appelé sommet **isolé**.

![Voisins](https://github.com/HackYourPhd/ateliers-open-geek/blob/master/Atelier_09/images/graphe-2.jpg)

EXO : Afficher le degré d'un sommet

EXO : Afficher la liste des voisins d'un sommet


#### Somme des degrés dans un graphe

A propos de sommets et de voisins, livrons nous à un petit exercice.

Imaginons 5 joueurs d’échecs, qui souhaitent organiser un tournoi entre eux. Peut-on trouver une liste de parties telle que chaque joueur affronte exactement 3 joueurs différents ?


On peut modéliser ce problème avec un graphe défini de la manière suivante :

- Chaque sommet représente un joueur
- Chaque arête représente un match entre deux joueurs.

Parvenez-vous à dessiner un tel graphe ?

![Un exemple avec des échecs](https://github.com/HackYourPhd/ateliers-open-geek/blob/master/Atelier_09/images/echecs.jpg)

Non ? C’est normal : cette construction est impossible. En effet, dans un graphe, la somme des degrés des sommets est forcément un nombre pair !

Pour s’en convaincre, il suffit de remarquer que chaque arête relie entre eux deux sommets : par conséquent, pour chaque arête, cette somme des degrés des sommets augmente de 2.

Il existe de nombreuses propriétés qui lient les différents composants d’un graphe : l’idée de cette séance n'est pas de vous en présenter un maximum, mais sachez que de nombreux chercheurs y consacrent encore leurs journées ! 

EXO : Calculer la somme des degré des sommets dans un graphe


#### Structures de données pour représenter un graphe

Il existe plusieurs façons de représenter un graphe.

Pour chaque sommet, on a généralement un identifiant numérique (ainsi parfois qu’un libellé ou d’autres caractéristiques).

Pour les aretes, on retrouve notamment les deux approches suivantes :

- Liste de voisins: On peut créer une liste pour chaque sommet, qui contient la liste des sommets adjacents à ce sommet
- Matrice de voisinage : On créé une matrice carrée de taille ***N***, où ***N*** est le nombre de sommets dans le graphe, et on note dans la case *(i,j)* la présence d'une arête entre les sommets *i* et *j*

La première approche sera par exemple intéressante dans le cas d'un graphe contenant peu d'arêtes (on parle de graph peu *dense*, ou de graphe *creux*).

EXO : Passer d'une représentation en listes à une représentation matricielle

EXO : Passer d'une représentation matricielle à une représentation en listes


### 5. Composantes connexes

#### Chaînes, cycles et arbres

Une **chaîne** (ou moins formellement **chemin**) dans un graphe est une suite d'arêtes consécutives, c'est-à-dire telle que chaque arête a une extrémité en commun avec la suivante.

Un **cycle** est une suite d'arêtes consécutives dont le sommet de départ et le sommet d'arrivé sont identiques.

Par exemple, sur le schéma ci-dessous, une chaîne est représentée en vert, et des cycles sont représentés en bleu et en rouge :

![Exemples de cycle](https://github.com/HackYourPhd/ateliers-open-geek/blob/master/Atelier_09/images/cycles.gif)

*Image : Kiatdd CC-BY-SA*


#### Cercles de connaissances

Le graphe ci-dessous représente un ensemble d'individus :

- Chaque sommet représente un individu
- Si deux sommets sont reliés par une arête, les deux personnes se connaissent

![Connexité](https://github.com/HackYourPhd/ateliers-open-geek/blob/master/Atelier_09/images/connexite.png)

Au-delà des connaissances directes, on peut voir que ce graphe permet de représenter des cercles de connaissances. Par exemple, à qui Léa peut-elle faire passer un message ? Et qu'en est-il d'Hélène ?


#### Les six degrés de séparation

**Les six degrés de séparation** est une théorie par Frigyes Karinthy en 1929, selon laquelle, pour tout couple d'individu sur le globe, on peut trouver une chaîne de relations individuelles de longueur au plus 6 reliant ces deux individus.

Bien que n'étant pas considéré comme scientifiquement valable, cette théorie illustre le degré de connection de nos sociétés, en particulier avec le développement des nouvelles technologies de communication, et les réseaux sociaux.

En 2011, Facebook annonçait dans une étude sur ses utilisateurs que 99.6% (resp. 92%) de ses utilisateurs pouvaient se connecter à un autre internaute en 5 (resp. 4) "degrés de séparation".


#### Connexité

Plus formellement, un graphe est dit **connexe** si pour tout couple de sommets de ce graphe, il existe un chaîne (c'est-à-dire une suite d'arêtes consécutives) entre ces deux sommets.

Une **composante connexe** d'un graphe est une sous-partie connexe maximale de ce graphe, c'est-à-dire :

- Un sous-ensemble de sommets, et les arêtes qui les relient entre eux
- Tel que ce sous-ensemble soit connexe : pour tout couple de sommet de ce sous-ensemble, il existe une chaîne entre ces deux sommets
- Tel qu'il ne soit pas possible d'ajouter un sommet à ce sous-ensemble tout en conservant cette connexité

EXO : Tester si deux sommets sont voisins

EXO : Tester si deux sommets appartiennent à la même composantes connexe (avec peut-être des indications/indices sur comment le faire ?)
 

#### Arbres

Un graphe connexe qui ne contient aucun cycle est appelé un **arbre** :

![Un exemple d'arbre](https://github.com/HackYourPhd/ateliers-open-geek/blob/master/Atelier_09/images/arbre.png)

Cette famille de graphes a de nombreuses propriétés, notamment en terme de hiérarchisation de l'information (on peut fixer un sommet "racine" et parcourir l'arbre à partir de ce sommet-là).


### 6. Parcours dans un graphe

#### Parcours en profondeur et parcours en largeur

![Parcours en profondeur](https://github.com/HackYourPhd/ateliers-open-geek/blob/master/Atelier_09/images/parcours-profondeur.png)

*Image : Alexander Drichel CC-BY-SA*

EXO : Lister tous les sommets parcours (parcours en profondeur)


![Parcours en largeur](https://github.com/HackYourPhd/ateliers-open-geek/blob/master/Atelier_09/images/parcours-largeur.png)

*Image : Alexander Drichel CC-BY-SA*

EXO : Lister tous les sommets parcourus (parcours en largeur)
 

#### Calcul du plus court chemin

On parlait de réseau routier au début de ce cours :

Dans un graphe 

![Parcours](https://github.com/HackYourPhd/ateliers-open-geek/blob/master/Atelier_09/images/parcours.png)

*Image : Artyom Kalinin CC-BY-SA*

#### Algorithme de Dijsktra

EXO : Calcul du plus court chemin dans un graphe étiquetté


### 7. Problèmes célèbres sur les graphes (avec des exos à chaque fois)

Graphes planaires

Parcours eulériens (fermés, ouverts)

Coloration


### 8. Quelques exemples concrets de l'utilisation des graphes sur des sujets de recherche



### 9. Des questions : que faire ?

- découvrez des tutoriels avancés (cf. ressources à la fin de ce billet)
- suivez d'autres formations dans vote université ou avec HYPhD ;)
- contactez-nous !


### 10. Ressources supplémentaires

- France IOI - Chapitres sur les graphes et les arbres : http://www.france-ioi.org/algo/chapters.php (attention, il vous faudra valider les premiers niveaux pour accéder à ces ressources)


Fiche réalisée par Constance de Quatrebarbes et Romain André-Lovichi (licence CC-BY-SA)
