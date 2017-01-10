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

- Formateurs : Romain André-Lovichi & Constance de Quatrebarbes

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

#### Graphes étiquettés

Il arrive souvent qu'on ajoute des étiquettes sur les arêtes d'un graphe : on parle alors de **graphe étiquetté** (ou **graphe pondéré**).

Ces étiquettes permettent en général de qualifier la relation entre les deux sommets :
- Distance entre deux villes
- Type de relation entre deux individus
- Capacité de transfert d'un tuyau reliant deux lieux

![Graphe orienté](https://github.com/HackYourPhd/ateliers-open-geek/blob/master/Atelier_09/images/graphe-etiquettes.jpg)

Dans le cadre de cette séance, on commencera par s'intéresser aux graphes non étiquettés, puis nous viendrons aux étiquettes (en particulier pour le calcul du plus court chemin).

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

**Préliminaires** : [Installer et importer les bibliothèques dans un script](./solutions/install.md):

voir les [instructions](./solutions/install.md)

**Exercice 01**: Recopier [cet exemple](./solutions/exo1.py) pour afficher un graphe

```python
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
```

**Exercice 02**: Construire un graphe à partir de cet énoncé:

    Dans les années 1830, le Duc de Densmore
    (aussi surnommé Barbe Bleue pour son exceptionnel capacité à se remarier)
    périt dans l'explosion qui détruisit son château.
    Son testament fut détruit ; or celui-ci avait tout pour déplaire à l'une de ses sept ex-femmes.

    Peu avant le crime, elles étaient toutes venues au château et elles jurèrent que ce fut la seule fois
    où elles s'y étaient rendues.
    Elles peuvent donc toutes être coupables,
    mais le dispositif ayant provoqué l'explosion
    avait été dissimulé dans une armure dans la chambre du Duc, et sa pose avait nécessité plus d'une visite.
    Donc la coupable a menti : elle est venue plusieurs fois.
    Dans leur déclarations aux enquêteurs:

    Ann dit avoir rencontré Betty, Charlotte, Félicia et Georgia;

    Betty dit avoir rencontré Ann, Charlotte, Edith, Félicia, et Helen ;

    Charlotte dit avoir rencontré Ann, Betty et Edith ;

    Edith dit avoir rencontré Betty, Charlotte et Félicia;

    Félicia dit avoir rencontré Ann, Betty, Edith et Helen;

    Georgia dit avoir rencontré Ann et Helen ;

    Helen dit avoir rencontré Betty, Félicia et Georgia.

    Créer le graphe de relations entretenues entre les sept ex-femmes.
    Nous verrons au cours de ce tutoriel comment trouver la coupable dans les exercices suivants

- Lister les sommets
- Lister les liens entre eux
- Afficher le graphe

**Exercice 03**: Créer une fonction build_graph(csv_f_name) qui à partir d'un fichier CSV renvoie un graph. Utiliser le fichier (./miserable.csv) pour construire le graphe des relations entre les personnages. Le fichier est structuré comme suit:
Nom1, Nom2, Nombre d'apparitions conjointes, XXX


### 4. Notions de voisinages

#### Voisins et degrés

Le **degré** d'un sommet est :

- le nombre d'arêtes partant de ce sommet
- le nombre de voisins de ce sommet
- la taille du voisinage de ce sommet

Un sommet de degré 0 (sans aucun voisin) est appelé sommet **isolé**.

![Voisins](https://github.com/HackYourPhd/ateliers-open-geek/blob/master/Atelier_09/images/graphe-2.jpg)

**Exercice 04**:  Créer une *fonction*  qui, à partir d'un graphe et d'un nom de sommet,
donne l'ordre de ce sommet `get_order(graph, "Edith")`
Testez-la sur les deux graphes à votre disposition
=> Astuce: importer le graph "barbe_bleue" à partir de votre fichier d'exercice
ex02.py
`from ex02 import g as graph_barbe_bleue`

=> Astuce: importer la fonction "build_graph()" depuis votre fichier d'exercice ex03.py
`from ex03 import build_graph`

**Exercice 05**: Créer une fonction 'get_neighbours(graph, "Mme.Thenardier") qui à partir d'un graphe et d'un sommet afficher la liste des voisins de ce sommet
Testez-la sur les deux graphes à votre disposition

#### Somme des degrés dans un graphe

A propos de sommets et de voisins, livrons nous à un petit exercice.

Imaginons 5 joueurs d’échecs, qui souhaitent organiser un tournoi entre eux. Peut-on trouver une liste de parties telle que chaque joueur affronte exactement 3 joueurs différents ?


On peut modéliser ce problème avec un graphe défini de la manière suivante :

- Chaque sommet représente un joueur
- Chaque arête représente un match entre deux joueurs.

**Exercice 05A**: Construire le graphe de ce tournoi.
Parvenez-vous à dessiner un tel graphe ?

![Un exemple avec des échecs](https://github.com/HackYourPhd/ateliers-open-geek/blob/master/Atelier_09/images/echecs.jpg)

Non ? C’est normal : cette construction est impossible. En effet, dans un graphe, la somme des degrés des sommets est forcément un nombre pair !

Pour s’en convaincre, il suffit de remarquer que chaque arête relie entre eux deux sommets : par conséquent, pour chaque arête, cette somme des degrés des sommets augmente de 2.

Il existe de nombreuses propriétés qui lient les différents composants d’un graphe : l’idée de cette séance n'est pas de vous en présenter un maximum, mais sachez que de nombreux chercheurs y consacrent encore leurs journées !

**Exercice 06**: Créer une fonction get_graph_order() qui à partir d'un graphe renvoie la somme des degré des sommets de ce graphe


#### Structures de données pour représenter un graphe

Il existe plusieurs façons de représenter un graphe.

Pour chaque sommet, on a généralement un identifiant numérique (ainsi parfois qu’un libellé ou d’autres caractéristiques).

Pour les aretes, on retrouve notamment les deux approches suivantes :

- Liste de voisins: On peut créer une liste pour chaque sommet, qui contient la liste des sommets adjacents à ce sommet
- Matrice de voisinage : On créé une matrice carrée de taille ***N***, où ***N*** est le nombre de sommets dans le graphe, et on note dans la case *(i,j)* la présence d'une arête entre les sommets *i* et *j*

La première approche sera par exemple intéressante dans le cas d'un graphe contenant peu d'arêtes (on parle de graph peu *dense*, ou de graphe *creux*).

Très peu de langage de programmation supporte nativement le graphe comme type de données
et Python ne fait pas exception. C'est pour cela que nous avons chargé le module complémentaire networkx mais nous pouvons aussi reproduire la structure d'un graphe à travers un mode de représentation simple.

Essayons de voir dans un premier temps à partir de l'un de nos graphes précédents comment afficher pour chaque noeud la liste de ses voisins: l'implémentation classique par liste de voisinage correspond à celle-ci
```
graph_dict = {'A': ['B', 'C'],
            'B': ['C', 'D'],
            'C': ['D'],
            'D': ['C'],
            'E': ['F'],
            'F': ['C']}
```
soit un dictionnaire qui a pour clé un sommet et pour valeur une liste de sommets auxquels il est reliés

De la même manière une matrice représentant un graph s'apparente à cette structure:
```
graph_matrix = [['A','B',1], ['A','C', 1],['F', 'A', 0], ...]

```

**Exercice 07** : Ecrire un script qui pour un graph donné renvoie un dictionnaire ou à chaque sommet correspond la liste des sommets auquel il est relié

```
def build_graph_dict(g):
'''transformer un graphe en un dictionnaire de listes'''
  graph = {}
  for node in g.nodes():
    ...
  return graph
```

**Exercice 08**: Ecrire un script qui pour un graph donné renvoie une matrice: soit toutes les arêtes possibles et si les sommets sont reliés ou non (0: pas reliés, 1: relié)

```
#importons la librairie
# qui nous permet de lister toutes les combinaisons possibles de somments
from itertools import combinations
def build_graph_mx(g):
'''transformer un graphe en une listes de liste'''
  graph = []
  all_edges = [[node1, node2] for node1, node2 in combinations(2, g.nodes())]
  for combo in all_edges:

    ...
  return graph

```



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
elles sont donc voisines

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

Exercice 09: Créez une fonction qui renvoie `True` si les deux sommets sont voisins et `False` dans le cas contraire


**Exercice 10**: Ecrire une fonction qui renvoie `True` si deux sommets appartiennent à la même composante connexe et `False` dans le cas contraire.

Explications: Ici on nous demande d'écrire une fonction qui vérifie qu'un chemin quelconque relie les deux sommets en effectuant un trajet du point A au point B qui ne doit passer repasser par le même sommet. Pour se faire, il s'agit d'implémenter:

- tout d'abord une fonction `find_path` qui propose un chemin possible d'un point A à un point B par voisinage.
Attention cet algorithme ne propose qu'un seul chemin: les résultats vont donc être aléatoires et différents à chaque appel!
Pourquoi? Parce que l'algorithme va commencer par un voisin de manière aléatoire.

![A vos neurones!](https://media3.giphy.com/media/aji7IPRbkeExO/200.gif#33) source:GIPHY

```
>>> Un peu d'aide?
# pseudocode pour trouver un chemin
def find_path(g, debut, fin, chemin=[])
  on ajoute le début au chemin
  si cible est la même que le sommet courant:
    #on est à la fin !
    retourner le chemin
  si le graphe n'a pas pour sommet le debut:
    il n'y a pas de chemin!

  pour chaque voisin du graphe en commencant par le debut:
    si le voisin n'est pas dans le path:
      et si  le voisin n'est pas la cible
        ajouter le voisin dans le chemin
        continuer à dérouler
  une fois tout les voisins testés si le chemin n'a pas été renvoyé
  il n'y pas de chemin!
```
![Alors?](https://media1.giphy.com/media/OueJX99V7zWla/200.gif#88)

La [solution](./solution/exo10_a.py) que l'on propose est  implique de tester les chemins un par un, c'est une opération longue et couteuse plus le graphe est grand plus elle est lente à mesure que s'accroît la complexité.

- ensuite d'étendre cette fonction pour stocker tous les chemins possibles de A -> B
Proposez une solution pour renvoyer tous les chemins de A -> B!

!(https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Don't_Panic.svg/2000px-Don't_Panic.svg.png) Source WikiCommons
La solution est par [ici](./solutions/ex10_b.py)

Mais **PAS DE PANIQUE!**, `networkx` a implementé une fonction. Si vous avez trouvé vous pouvez vérifier votre résultat et
appeler la [fonction correspondante](https://networkx.readthedocs.io/en/stable/reference/generated/networkx.algorithms.simple_paths.all_simple_paths.html#networkx.algorithms.simple_paths.all_simple_paths) de networkx pour votre graphe

Sinon vous pouvez toujours utiliser une fonction déjà implementée ;)
``` python
#!usr/bin/python3
import networkx as nx

paths = nx.all_simple_paths(g, nodeA, nodeB)
print(list(paths))

```

- et enfin il s'agit de vérifier si le chemin entre A et B existe bien dans le graph en créant la fonction ```has_path(graph, nodeA, nodeB)```

![](https://media3.giphy.com/media/BBkKEBJkmFbTG/200.gif#91)
La solution par [ici](./solutions/ex_10_c.py)!

Evidemment, elle existe aussi en networkx
``` python
#!usr/bin/python3
import networkx as nx

print(nx.has_path(graph, nodeA, nodeB))

```

#### Arbres

Un graphe connexe qui ne contient aucun cycle est appelé un **arbre** :

![Un exemple d'arbre](https://github.com/HackYourPhd/ateliers-open-geek/blob/master/Atelier_09/images/arbre.png)

Cette famille de graphes a de nombreuses propriétés, notamment en terme de hiérarchisation de l'information (on peut fixer un sommet "racine" et parcourir l'arbre à partir de ce sommet-là).


### 6. Parcours dans un graphe

Un graphe contient souvent des dizaines, voire même des centaines ou des milliers de noeuds. Il devient alors intéressant d'*explorer* ce graphe.

Il existe différentes approches pour explorer un graphe : on parle souvent de **parcours**. Selon les circonstances, l'objectif pourra être de passer par tous les sommets du graphe, ou plutôt d'atteindre un sommet en particulier.

#### Parcours en profondeur

Un *parcours en profondeur* est une méthode assez "naturelle" de parcours d'un graphe ou d'un arbre : on avance de sommet en sommet, et on continue tant qu'on trouve des sommets qu'on n'a pas encore "visité".

Lorsqu'on arrive à un sommet dont tous les voisins ont déjà été visités, on revient en arrrière jusqu'à l'intersection précédente, et on reprend l'exploration à partir de là.

Ce type de parcours s'illustre bien sur un arbre :

![Parcours en profondeur](https://github.com/HackYourPhd/ateliers-open-geek/blob/master/Atelier_09/images/parcours-profondeur.png)

*Image : Alexander Drichel CC-BY-SA*

EXO : Lister tous les sommets parcours (parcours en profondeur)


#### Parcours en largeur

Un *parcours en largeur* repose sur une approche très différente : on visite d'abord tous les sommets situés à distance 1 du sommet de départ, puis tous les sommets situés à distance 2, etc.

Là encore, Ce type de parcours s'illustre bien sur un arbre :

![Parcours en largeur](https://github.com/HackYourPhd/ateliers-open-geek/blob/master/Atelier_09/images/parcours-largeur.png)

*Image : Alexander Drichel CC-BY-SA*

EXO : Lister tous les sommets parcourus (parcours en largeur)


#### Calcul du plus court chemin

Comme on l'a vu au début de cette séance, les cartes routières sont un exemple simple de graphes faisant partie de notre vie quotidienne. Et quand on parle de carte routière, on se demande généralement quel est le **plus court chemin** entre un point A et un point B.

Et comme vous l'avez sans doute remarqué si vous avez déjà pris le volant, entre les embouteillages, les sens uniques, et les différents types de voies, ce plus court chemin est rarement la ligne droite.

On peut représenter toutes ces contraintes avec un graphe orienté et étiquetté par des temps de trajet :

![Parcours](https://github.com/HackYourPhd/ateliers-open-geek/blob/master/Atelier_09/images/parcours.png)

*Image : Artyom Kalinin CC-BY-SA*

L'objectif est alors de trouver dans ce graphe une chaîne partant du sommet de départ et arrivant au sommet d'arrivée, de telle sorte à ce que la somme des étiquettes soit minimale.

Pour calculer ce plus court chemin, on peut notamment utiliser l'**algorithme de Dijsktra**. Vous pourrez en trouver une présentation détaillée ici : https://fr.wikipedia.org/wiki/Algorithme_de_Dijkstra

EXO : Calcul du plus court chemin dans un graphe étiquetté


### 7. Problèmes célèbres sur les graphes (avec des exos à chaque fois)

La théorie des graphes est une domaine vaste, avec des thématiques variées.

Voici donc, pour ceux qui voudraient aller un peu plus loin, quelques problèmes célèbres sur les graphes.

#### Graphes planaires

Sur la figure ci-dessous, est-il possible de relier chaque point bleu (en haut) à chaque point (jaune), sans qu'aucun trait n'en croise un autre ?

![K3,3](https://github.com/HackYourPhd/ateliers-open-geek/blob/master/Atelier_09/images/K33.jpg)

Dans le même ordre d'idée, est-il possible de relier chacun des 5 points ci-dessous aux 4 autres, sans qu'aucun trait n'en croise un autre ?

![K5](https://github.com/HackYourPhd/ateliers-open-geek/blob/master/Atelier_09/images/K5.jpg)

Ces deux problèmes sont liés à une famille particulière de graphes : les **graphes planaires**. Un graphe est dit planaire s'il existe une représentation dans le plan de ce graphe telle qu'aucune arête n'en croise une autre.

Il se trouve que les deux graphes ci-dessus ne sont pas planaires, ce qu'on peut prouver grâce à la théorie des graphes. On peut donc ainsi démontrer qu'il n'y a pas de solution aux deux questions ci-dessus.


#### Parcours eulériens

Vous avez peut-être déjà entendu parler de la ville de Königsberg ? Il s'agissait d'une ville de Prusse (aujourd'hui Kaliningrad), traversée par la rivière.

Cette ville comportait notamment 7 sept ponts, reliant entre eux deux îles et les deux rives de la rivière :

![Les ponts de Königsberg](https://github.com/HackYourPhd/ateliers-open-geek/blob/master/Atelier_09/images/ponts-1.png)

*Image : Bogdan Giuşcă, CC-BY-SA*

Selon vous, un habitant peut-il faire un trajet dans la ville en passant exactement une fois par chacun des ponts (sans traverser à la nage ;) ) ?


Dans le même ordre d'idée (même si ce n'est pas évident a priori), pensez-vous pouvoir tracer le dessin ci-dessous sans lever votre stylo (et sans repasser deux fois par le même trait) ? Et en revenant à votre point de départ ?

![Sans lever le stylo ?](https://github.com/HackYourPhd/ateliers-open-geek/blob/master/Atelier_09/images/enveloppe-1.jpg)


Ces deux questions sont en fait liéés à la notion de **parcours eulérien** dans un graphe, c'est à dire un cycle passant exactement une fois par chacune des arêtes.

Voici les graphes correspondants à ces deux situations :

![Les ponts de Königsberg - Version graphe](https://github.com/HackYourPhd/ateliers-open-geek/blob/master/Atelier_09/images/ponts-2.jpg)

![Sans lever le stylo ? - Version graphe](https://github.com/HackYourPhd/ateliers-open-geek/blob/master/Atelier_09/images/enveloppe-2.jpg)

Le théorème d'Euler nous indique qu'un graphe connexe admet un parcours eulérien si et seulement si tous ses sommets sont de degré pair.

Si on s'autorise à avoir une chaîne plutôt qu'un cycle (le sommet de départ et le sommet d'arrivée ne sont pas forcément identiques), on peut avoir deux sommets de degré impair.

C'est la raison pour laquelle il n'y a pas de solution au problème des sept ponts de Königsberg, et pour laquelle on peut tracer une enveloppe sans lever son stylo, mais pas en revenant à son point de départ.


#### Coloration

La plupart des cartes du monde sont faites de telle sorte que deux pays voisins ne sont pas de la même couleur :

![Carte du monde](https://github.com/HackYourPhd/ateliers-open-geek/blob/master/Atelier_09/images/carte.jpg)

Cette propriété, qui n'est pas si triviale, est liée à la **coloration des graphes** : comment affecter une couleur à chacun des sommets d'un graphe, de telle sorte que deux sommets voisins n'aient jamais la même couleur.

![Coloration de graphe](https://github.com/HackYourPhd/ateliers-open-geek/blob/master/Atelier_09/images/coloration.png)


### 8. Quelques exemples concrets de l'utilisation des graphes sur des sujets de recherche

http://data.bnf.fr/semanticweb


### 9. Des questions : que faire ?

- découvrez des tutoriels avancés (cf. ressources à la fin de ce billet)
- suivez d'autres formations dans vote université ou avec HYPhD ;)
- contactez-nous !


### 10. Ressources supplémentaires

- France IOI - Chapitres sur les graphes et les arbres : http://www.france-ioi.org/algo/chapters.php (attention, il vous faudra valider les premiers niveaux pour accéder à ces ressources)


Fiche réalisée par Constance de Quatrebarbes et Romain André-Lovichi (licence CC-BY-SA)
