`Atelier 03`
# Manipuler du texte en Python

## Qu'est ce qu'un texte en Python?
    C'est un `type de données` qu'on appelle `string`
Un ensemble de caractères stockés les uns à la suite des autres une chaine de caractères

Dans le terminal on voit que Python comprend bien le texte si on lui indique avec des guillemets et que la commande nous indique
que c'est un type `str` soit une `string` chaine de caractères
```
>>> hello world
File "<stdin>", line 1
    hello world
              ^
SyntaxError: invalid syntax
>>> "hello world"
'hello world'
>>> type("hello world")
<type 'str'>
```
Jusque là rien de très sorcier
On peut le stocker dans une variable
et lui demander de l'afficher avec la fonction `print`

```
>>> salut= "hello world"
>>> print(salut)
'hello world'
>>>
```

#### La chaine de caractère

Comme ce sont des caractères les uns à la suite des autres, le texte est stocké de la même manière qu'une `liste`.

Pour savoir combien de lettres dans ma phrase
on utilise une fonction déjà existante

```
>>> print len(salut)
10
>>>
```
Attention l'espace compte pour un caractère **car c'est un caractère**.

Pour avoir la première lettre on demande le premier element dans la liste
```
>>> print(salut[0])
'h'
>>>
```
On peut lui demander le deuxième le troisième et le dernier
```
>>> print(salut[1])
'e'
>>> print(salut[2])
'l'
>>> print(salut[-1])
'd'
```

On peut aussi lui demander
les 3 premiers lettres et les trois dernières
```
print(salut[0:2])
print(salut[-3:-1])
```

##### Manipulation du texte

Comme string est un type de données lui est attachée un ensemble de `fonction` propres à la string. Pour en voir toutes la liste: rendez vous sur la [documentation de string](https://docs.python.org/3/library/stdtypes.html#string-methods)

* on peut les unir ensemble avec l'opérateur `+`:

  `"hello"+"open geeks"`
* multiplier les chaines de caractères avec l'opérateur `*`:

  `"good morning!"*3`

* changer la casse avec les méthodes:

  - `upper()`
  - `lower()`
  - `title()`

* remplacer, modifier supprimer des lettres
- `replace()`


salut = "hello world"
salut.replace("world", "everybody")
salut.replace("l", "*")

* découper ou recoller (concaténer)
texte = "je suis une suite de mots séparés par des espaces"
words = texte.split(" ")
print(words)
hashtags = ("#").join(words)
print(hashtags)

Découper le texte en séquences de mots clés peut etre très utile pour analyser un texte.

Pour le réutiliser plus facilement on va créer une fonction get_keywords() qui prend n'importe quel texte et retourne une liste de mots-clés.
Nous allons l'améliorer par la suite...

```
def get_keywords(text):
  '''fonction qui prend en entrée du texte str et retourne en sortie une liste '''
  keywords = text.split(" ")
  return keywords
```
qu'on peut aussi simplifier sans passer par un stockage dans une variable
```
def get_keywords(text):
  '''fonction qui prend en entrée du texte str et retourne en sortie une liste '''
  keywords = text.split(" ")
  return Keywords

```
Voilà, notre fonction est prête on va pouvoir l'utiliser (en informatique on parle d'instancier une fonction) autant de fois qu'on veut

```
proverbe = get_keywords("La vie n'est pas un long fleuve tranquille")
print(proverbe)
proverbe2 = "QUi troP embrasse mal Etreint"
print(get_keywords(proverbe2))
```

Maintenant que nous avons vu un ensemble de manipulation basique à vous de jouer...

1. Créer une fonction `clean_text()` qui prend un texte en entrée et renvoie un texte où tous les caractères non alphabétique (espace, nombres, ponctuation) ont été transformé en espace et en minuscule.

2. Créer une fonction `count_keywords()` qui prend un texte en entrée et renvoie le nombre de mots clés dans la phase



### Les boucles
Comme la string est une `liste` de caractère on peut aussi utiliser les fonctions des listes qui existent déjà.

Comme nous avons vu on peut accéder au caractères d'un mot ou d'une phrase selon sa position. Cela marche de la même manière avec les listes:
```
liste = ["pommes", "poires", "bananes", "oranges"]
#Donne moi le premier élement de ma liste
liste[0]
#Le deuxième
liste[1]
#Le dernier
liste[-1]
```
On peut aussi dérouler un par un les élements d'une liste en utilisant l'instruction `for`
```
for element in liste:
  print(element, "compte", len(element), "lettres")
```
Dans l'exercice 2, on demandait d'imprimer l'alphabet puis l'alphabet à l'envers
Essayons maintenant d'imprimer les lettres de l'alphabet sur une ligne
```
for lettre in "abcdefghijklmnopqrstuvwxyz":
  print(lettre)
```
A vous d'afficher maintenant les lettres dans le sens inverse de l'ordre alphabetique
Indice: une chaine de caractère peut etre mise en sens inverse... tout comme une liste.

### Les conditions

Python permet de créer des conditions et appliquer un comprtement différents en fonction de ces conditions

if "a" in word:


Evidemment ca n'est que le début, afficher l'aphabet sur une ligne, présente un intérêt assez limité,
en revanche pouvoir appliquer des calculs ou des tests de la même manière à tous les élements d'une liste peut s'avérer extrèmement pratique à l'usage. On le voit dans le premier exemple de boucle:
on peut afficher un element mais aussi calculer le nombre de lettre de chaque mot ou encore appliquer un comportement différent en fonction d'une condition.


### Les dictionnaires

Quelques exercices de manipulation du texte
* Dictionnaire

Manipuler du texte est très utile en bioinformatique: les chaines ADN sont en effet elles aussi des chaines de caractères.
Voyons donc quels usages on peut en faire avec quelques [exercices de bioinformatique
[Exercices en bioinformatique exercice avec l'ADN
Et quelques revisions des notions que nous avons abordées rapidement

### Textmining: procédure
* Petit rappel: le *textmining* ou la fouille de texte implique de sortir la pelle, la pioche, les ciseaux le marteau on se concentre sur la **forme** des mots et non sur le sens. On utilise les règles:
  * de morphologie
  * de grammaire
  * de syntaxe

L'ensemble de motifs que l'on peut observer dans leur apparition. Les traitements qu'on fait dessus sont des traitements **statistiques** et non pas **sémantiques**.

On parle alors de `traitement automatique de langue` (TAL) ou en anglais Natural Langage Processing (NLP). Il s'agit bien d'observer l'ensemble des faits statistiques d'un corpus de données et d'en tirer des conclusions.
On s'éloigne en cela de la sémantique qui regarde à quoi les mots réfèrent et leur relation de sens.

||LINGUISTIQUE|SEMANTIQUE|
|: | :| :|
|Ce qu'on regarde|**forme**| **sens**|
|Exemple| invention, inventeur, inventer| exact, vrai, correct
|Type d'observation | pluriel, verbe, adjectifs| synonyme, antonyme|
| Procédé | forme/ motif /règles/occurences/position | reférence/catégorie/lien/sens|
|Approche méthodologie| Enquête statistique et induction| Croisement de données et déduction |
||Fréquence, décompte| Ontologie et hiérarchie|

Un dernier exemple:
un traitement statistique ne nous permettra pas dans un premier temps de répondre automatiquement à la question: Quelle est la couleur du cheval blanc d'Henri IV?

En revanche on pourra déterminer qu'il s'agit d'une question en se concentrant sur le signe '?', déterminer la longeur de la phrase, garder les mots-clés tels que les noms communs et leur position dans la phrase ou  encore analyser des occurences .

Si le traitement sémantique vous intéresse il peut faire l'objet d'un autre atelier pour faire vite le fonctionnement repose sur des 'dictionnaires' des tables de références un peu particulières qu'on appelle des ontologies. Les archivistes et bibliothécaires travaillent à la constitution de ces ontologies.
Les technologies du Web Sémantique par exemple utilise une manière particulière de stocker les informations sous forme de triplet SUJET PREDICAT OBJET qui souligne le type de relation qu'entretiennent le sujet et l'objet.

Le cheval est blanc relie un animal à une couleur par une relation d'identité.
Dans le cas d'un livre dans une bibliothèque il est classé par thématique, par époque et ensuite par auteur (ordre alphabétique). Un plan de classement qui suit un ou plusieurs standard. Le XML-TEI reprend ces concepts et les applique au texte.

Mais traiter un corpus textuel requiert avant ce type d'analyse un peu plus poussé du traitement automatique de langue traditionnellement issu de la linguistique informatique (statistiques)

### Ou trouve t-on du texte?

* input(): lire de données entrées par l'utilisateur
* variable: copier coller un texte
* document: lire un fichier
* base de données: récupérer des données par requete et Croisement
* web, mail, logs

### Textmining: les étapes
Les principales étapes pour une enquête sur un corpus de données textuelles sont:
* parsing
* nettoyage et formatage
* segmentation
* etiquetage
* classification
* analyse

#### Parsing
* le `parsing` lecture et sauvegarde: soit parcourir et enregister le texte de manière à ce qu'on puisse facilement y accéder

Lire et écrire un fichier
Dans l'atelier 1, vous avez vu comment accéder au fichier avec Python. Ici nous allons lire un fichier
```
def read_file(file_name):
  '''lire un fichier'''
  with open(file_name, "r") as f:
    data = f.read()
    return data

def write_file(filename, data):
  '''ecrire un fichier'''
  with open(file_name, "w") as f:
    f.read()
    return file_name

```


EXERCICE 07
EXERCICE 08
* le `formatage` et le nettoyage: nettoyer et convertir pour s'assurer que le texte a une forme manipulable facilement et transférable selon un standard.
On utilise pour cela les méthodes propres au texte, ou liste et aussi un langage/notation/racourci pour détecter des motifs dans le but de produire un texte dans un format particulier et détecter ce qui nous intéresse.

=> **Regex** , la voie "royale"?


* la `segmentation` le découpage et la simplification: segmentation/ tokenisation/ balisage/ stemming : découper le texte en petite unité lexicale ou syntaxique et simplifier les formes:
  - mots clés
  - ngrams
  - forme simplifiée

=> **NLTK**, la boite à outil en python pour le TAL
* le `filtrage`, l'`étiquetage et la categorisation`:

  - motifs récurrents
  - catégorie grammaticale
  - champs lexicaux

* l'`indexation et le classement`
pour mettre en contexte
à ce stade on utilise:
  *  les métadonnées ou données contextuelles de notre corpus comme les champs descriptifs ou la source
  * des tables de correspondances (dictionnaires, base de données) produites par des tiers et enrichie automatiquement à partir de corpus qui permettent de classer.
  * des algorithmes et des méthodes statistiques pour chercher, ranger, classer

On applique ensuite un ensemble de traitements en fonction de l'analyse qu'on souhaite faire et du contexte qu'on veut prendre en compte pour dégager des caractéristiques du texte ou faire emerger un ordre.

* Reconnaissance d'entités nommées
* Extraction de relations
* Résumé automatique
* Analyse factorielle de correspondances
* Analyse de sentiment
