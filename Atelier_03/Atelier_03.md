`Atelier 03`
# Introduction à Python (1)
`Atelier 03`
## Manipuler du texte en Python

### Qu'est ce qu'un texte en Python?

    C'est un `type de données` qu'on appelle `string`
Un ensemble de caractères stockés les uns à la suite des autres une chaine de caractères.

Il existe de nombreux types de données les plus utilisées
sont:
* les entiers (int)
* les décimaux (float)
* les chaines de caractères (string)
* les booléens

Il existe aussi des types de données composées qui pemettent de stocker plusieurs élements
parmi lesquels
* les listes (list) ["element", 2, True, ... ]
* les dictionnaires (dict) {clé: "valeur", ...}
* les tuples (tuple) (1,2)

Nous avons choisi ici d'introduire python par la chaine de caractère

#### String

Dans le terminal on voit que Python comprend bien le texte si on lui indique avec des guillemets et que la commande nous indique
que c'est un type `str` soit une `string` chaine de caractères.
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
On peut le stocker dans une `variable`
et lui demander de l'afficher avec la fonction `print`

```
>>> salut= "hello world"
>>> print(salut)
'hello world'
>>>
```
La fonction print est une fonction standard qui permet d'affficher une donnée en entrée (input)

##### Manipulation du texte: les fonctions de strings

Comme string est un type de données lui est attaché un ensemble de `méthodes` propres à la string.
Pour en voir toutes la liste : rendez vous sur la [documentation de string](https://docs.python.org/3/library/stdtypes.html#string-methods)

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

```
salut = "hello world"
salut.replace("world", "everybody")
salut.replace("l", "*")
salut.replace("w", "")
```

* découper ou rejoindre des morceaux de texte
```
texte = "je suis une suite de mots séparés par des espaces"

words = texte.split(" ")
print(words)
hashtags = ("#").join(words)
print(hashtags)
```

#### La chaine de caractère

Comme ce sont des caractères stockés les uns à la suite des autres.
Le texte (string) est stocké de la même manière qu'une `liste`.
Un liste c'est un type de données qui permet de stocker des élements les uns à la suite des autres.

Pour savoir combien de lettres dans ma phrase
on utilise une fonction déjà existante `len`

```
>>> print(len(salut))
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
On peut lui demander le deuxième le troisième et le dernier...
```
>>> print(salut[1])
'e'
>>> print(salut[2])
'l'
>>> print(salut[-1])
'd'
```

On peut aussi lui demander
les trois premières lettres et les trois dernières
```
print(salut[0:2])
print(salut[-3:-1])
```

#### Les fonctions.

Découper le texte en séquences de mots-clés peut être très utile pour analyser un texte.
C'est d'ailleurs une partie importante pour exploiter un texte : le transformer en liste de mots.

Pour le réutiliser plus facilement on va créer une fonction get_keywords() qui prend n'importe quel texte et retourne une liste de mots-clés.
Nous allons l'améliorer par la suite...

```
def get_keywords(text):
  '''fonction qui prend en entrée du texte str et retourne en sortie une liste '''
  keywords = text.split(" ")
  return keywords
```

qu'on peut aussi simplifier sans passer par un stockage dans une `variable`

```
def get_keywords(text):
  '''fonction qui prend en entrée du texte str et retourne en sortie une liste '''
  return text.split(" ")

```

Voilà, notre fonction est prête on va pouvoir l'utiliser autant de fois qu'on veut.
En informatique, on parle d'`instancier` une fonction.

```
proverbe = get_keywords("La vie n'est pas un long fleuve tranquille")
print(proverbe)
proverbe2 = get_keywords("QUi troP embrasse mal Etreint")
print(proverbe2)
print(get_keyword("avoir la flemme de donner un autre nom de variable et appeler directement la fonction")
```

### Les listes

Comme la string est une `liste` de caractère on peut aussi utiliser les fonctions des listes qui existent déjà.

Comme on l'a déjà vu, on peut donc accéder aux caractères d'un mot ou d'une phrase selon sa position. Cela marche de la même manière avec les listes:
```
liste = ["pommes", "poires", "bananes", "oranges"]
#Donne moi le premier élement de ma liste
liste[0]
#Le deuxième
liste[1]
#Le dernier
liste[-1]
```

### L'instruction for
On peut aussi dérouler un par un les élements d'une liste en utilisant l'instruction `for`

```
for lettre in "abcdefghijklmnopqrstuvwxyz":
  print(lettre)
```


Evidemment ca n'est que le début, afficher chaque lettre sur une ligne, présente un intérêt assez limité,
en revanche pouvoir appliquer des calculs ou des tests de la même manière à tous les élements d'une liste peut s'avérer extrêmement pratique à l'usage.
On le voit dans le premier exemple de boucle :
on peut afficher un element mais aussi calculer le nombre de lettres de chaque mot ou encore appliquer un comportement différent en fonction d'une condition.

```
liste = ["une", "phrase", "est", "un", "ensemble", "de", "mots", "enumeré", "les", "uns" "à", "la", "suite", "des", "autres"]
for mot in liste:
  print(mot, "compte", len(mot), "lettres")
```

Evidemment les listes étant un autre type de données y sont attachées de nombreuses fonctions.

Pour ajouter un element à la fin d'une liste:
* `liste.append(element)`
Pour insérer un element à un endroit précis de la liste:
* `liste.insert(element, 3)`
Pour supprimer un element précis de la liste
* `liste.remove(element)`
Pour enlever le 2ème element de la liste
* `liste.pop(1)`

On se sert énormément des listes pour stocker des données. Il est aussi très pratique de considérer un texte comme une liste.
Un livre n'est t'il pas une liste de tomes, chapitres, paragraphes, phrases, mots, caractères?

L'ADN est elle aussi à bien y regarder une chaine de caractères une liste.
La manipulation du texte est donc une opération esssentielle de la programmation.

### Les conditions

Ahh les conditions! Que ferait-on sans les conditions? Historiquement, en informatique, en electronique et en télécommunication: pas grand chose.
Un signal n'est il pas l'expression d'une condition ?

C'est la base de production du code binaire: si l'interrupteur est allumé = 1
si l'interrupteur est éteint = 0
C'est d'ailleurs aussi la base du code morse : signal court vs signal long qui sur les phares se réduisent à lumière/pas lumière

Dans la vraie vie qui ne s'est jamais confronté à ce genre de conditions?

Si la lumière est allumée: alors je peux rentrer
Si la lumière est éteinte: alors je ne peux pas rentrer.
Tentons une petite fonction pour modéliser le problème.

```
def canIenter?(light):
  if light == "on":
    return True
  else:
    return False
```

En logique on appelle ça de la logique booléenne.
Le type de données qu'on a utilisé ici est un booléen. (Du mathématicien et logicien George Boole)
Dans cette logique, il n'existe que deux états : soit c'est vrai, soit c'est faux. Un type booléen stocke donc les valeurs Vrai ou Faux

Evidemment ce mode de pensée binaire a ses limites...
C'est pourquoi on a évidemment le droit d'avoir des conditions beaucoup moins strictes et des retour de fonction beaucoup plus libres.
Ouf!

Prenons un exemple bien moins sexy
```
alphabet = "abcdefghijklmnopqrstuvwxyz"
voyelles = "aeiouy"

def estvoyelle(lettre):
  if lettre in voyelle:
    print(lettre, "est une voyelle")
    return True
  elif lettre in alphabet:
    print(lettre, "est une consonne")
    return False
  else:
    print(lettre, "n'est pas une lettre")
    return False

print(estvoyelle("a"))
print(estvoyelle("*"))
```

Voyons une autre fonction qui remplace les voyelles par une étoile et ne renvoie que les caractères alphabétiques.

```
alphabet = "abcdefghijklmnopqrstuvwxyz"
voyelles = "aeiouy"

def caviardage(texte):
    nouveautexte = []
    for lettre in texte:
        if lettre in voyelles:
            nouveautexte.append(lettre)

        elif lettre in alphabet:
            nouveautexte.append("*")
        else:
            pass
    return nouveautexte

print(caviardage("Oh! mais c'est une technique idiote de censure... Arriverais-je à lire le résultat?"))
```

### Les dictionnaires
Il existe aussi un manière de stocker du texte (entre autre). Une qui est très pratique et que les linguistiques adorent et donc les généticiens raffolent : les `dictionnaires`

Les dictionnaires sont des index ou des tables de correspondances.
Comme des vrais dictionnaires ils ont une seule entrée (une clé) et une information liée
(une valeur).
Les entrées du dictionnaires en python prennent n'importe quel type.

Voici un vrai dictionnaire alphabanumérique => morse stocké sous forme de dictionnaire python!

MORSE = {'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
     	'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.'
        }

A bien y regarder, l'ADN est une chaine de caractère à manipuler: [quelques exercices de bioinformatique](./Enoncés-Exercices-ADN.ipynb)

On peut aussi en fonction de son avancement regarder les exercices à faire dans cette liste (./exercices.md)
## Textmining Fouille de données textuelles

### Un peu de théorie
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
* variable: stocker une chaine de caractère
* document: lire un fichier
* web, mail, logs
* base de données: récupérer des données par requete et croisement pour extraire une information qualifiée


### Les étapes principales à la fouille et à l'analyse de texte
Les principales étapes pour une enquête sur un corpus de données textuelles sont:
* parsing
* nettoyage et formatage
* segmentation
* etiquetage
* classification
* analyse

Evidemment à chaque étape de traitement on vérifie les données de son corpus et qu'on a rien perdu au passage!

