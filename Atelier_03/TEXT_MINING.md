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

Comme string est un type de données lui est attachée un ensemble de `fonction` propres à la string.
Pour en voir toutes la liste: rendez vous sur la [documentation de string](https://docs.python.org/3/library/stdtypes.html#string-methods)

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
```

* découper ou rejoindre des morceaux de texte
```
texte = "je suis une suite de mots séparés par des espaces"

words = texte.split(" ")
print(words)
hashtags = ("#").join(words)
print(hashtags)
```

Avec ce que vous savez déjà, nous allons faire le traditionnel hello world.
Dans tout apprentissage informatique, on commence donc par saluer le monde
dans la langue que nous sommes en train d'apprendre.

 Afficher salut tout le monde !
 Remplacer salut tout le monde ! par salutation au soleil!
  Attention il y a plusieurs manière de faire...
> Afficher "salutation au soleil salutation au soleil salutation au soleil"
> Afficher "salut soleil salut soleil salut soleil"

#### Les functions
Découper le texte en séquences de mots clés peut être très utile pour analyser un texte.
C'est d'ailleurs une partie importante pour exploiter un texte: le transformer en liste de mots.

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
Voilà, notre fonction est prête on va pouvoir l'utiliser autant de fois qu'on veut
(en informatique on parle d'instancier une fonction)

```
proverbe = get_keywords("La vie n'est pas un long fleuve tranquille")
print(proverbe)
proverbe2 = get_keywords("QUi troP embrasse mal Etreint")
print(proverbe2)
print(get_keyword("avoir la flemme de donner un autre nom de variable et appeler directement la fonction")
```

Maintenant que nous avons vu un ensemble quelques manipulations basiques, quelques exercices

>>> Créer une fonction `clean_text()` qui prend un texte en entrée et renvoie un texte où tous les caractères non alphabétique (espace, nombres, ponctuation) ont été transformé en espace et en minuscule.

>>> Créer une fonction `count_keywords()` qui prend un texte en entrée et renvoie le nombre de mots clés dans la phase



### Les listes

Comme la string est une `liste` de caractère on peut aussi utiliser les fonctions des listes qui existent déjà.

On peut donc accéder au caractères d'un mot ou d'une phrase selon sa position. Cela marche de la même manière avec les listes:
```
liste = ["pommes", "poires", "bananes", "oranges"]
#Donne moi le premier élement de ma liste
liste[0]
#Le deuxième
liste[1]
#Le dernier
liste[-1]
```
On se sert énormément des listes pour stocker des données. Il est aussi très pratique de considérer un texte comme une liste.
Un livre n'est t'il pas une liste de tome, chapitre, paragraphe, phrase, mot?
L'ADN est elle aussi à bien y regarder une chaine de caractères une liste.

Voyons donc quels usages on peut en faire avec quelques [exercices de bioinformatique](./Enoncés-Exercices-ADN.ipynb)

Vous trouverez aussi pour vous entrainez un dataset tout simple que vous pouvez importer
- [Les 10 commandements](./decalogue.py)
- Faites une fonction qui affiche un commandement selon son numero
- Faites une fonction qui donne tous les commandement qui correspondent à un mot



### L'instruction for
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

Evidemment ca n'est que le début, afficher l'aphabet sur une ligne, présente un intérêt assez limité,
en revanche pouvoir appliquer des calculs ou des tests de la même manière à tous les élements d'une liste peut s'avérer extrèmement pratique à l'usage. On le voit dans le premier exemple de boucle:
on peut afficher un element mais aussi calculer le nombre de lettre de chaque mot ou encore appliquer un comportement différent en fonction d'une condition.

```
for element in liste:
  print(element, "compte", len(element), "lettres")
```

Evidemment les listes étant un autre type de données y sont attaché de nombreuses fonctions.

Pour ajouter un element à la fin d'une liste:
* `liste.append(element)`
Pour insérer un element à un endroit précis de la liste:
* `liste.insert(element, 3)`
Pour supprimer un element précis de la liste
* `liste.remove(element)`
Pour enlever le 2e element de la liste
* `liste.pop(1)`

### Les conditions

Ahh les conditions! Que ferait on sans les conditions? Historiquement, en informatique, en electronique et en télécommunication: pas grand chose. Un signal n'est il pas l'expression d'une condition ?

C'est la base de production du code binaire: si l'interrupteur est allumé = 1
si l'interrupteur est éteint = 0
C'est d'ailleurs aussi la base du code morse signal court signal long qui sur les phares se réduisent à lumière/pas lumière

Dans la vraie vie qui ne s'est jamais confronté à ce genre de conditions?
Si la lumière est allumée: alors je peux rentrer
Si la lumière est éteinte: alors je ne peux pas rentrer.
Evidemment, on n'est pas à l'abri du paradoxe mais passons.

```
def canIenter?(light):
  if light == "on":
    return True
  else:
    return False
```

En logique on appelle ca de la logique booléenne et le type de données qu'on a utilise ici est un booléen. (Du mathématicien et logicien George Boole) Dans cette logique il n'existe que deux états: soit c'est vrai, soit c'est faux.

Evidemment ce mode de pensée binaire a ces limites c'est pourquoi on a évidemment le droit d'avoir des conditions beaucoup moins strictes et des retour de fonction beaucoup plus libres.
Ouf!

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
    print(lettre, "n'est pas une consonne")
    return False

```
Ecrivons une fonction qui renvoie un texte avec tous les mots qui comptent plus de 3 lettres
s'ils ont trois lettres afficher le mots et le nombre de lettres, s'ils ont moins de 3 lettres
afficher "trop petit" et le mot.

def stop_words(texte):

  return texte

### Les dictionnaires
Il existe aussi un manière de stocker du texte (entre autre). Une qui est très pratique et que les linguistiques adorent:les dictionnaires qui sont des index ou des tables de correspondances.
Comme des vrais dictionnaires ils ont une seule entrée (une clé) et une information liée
(une valeur).
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


>>> Ecrivez une fonction qui prend un phrase et qui renvoie le code morse de cette phrase
>>> Bonus: Ecrivez la fonction inverse



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

Evidemment à chaque étape de traitement on vérifie les données de son corpus et qu'on a rien perdu au passage!

#### Parsing
* le `parsing` lecture et sauvegarde: soit parcourir et enregister le texte de manière à ce qu'on puisse facilement y accéder

Lire et écrire un fichier
Dans l'atelier 1, vous avez vu comment accéder au fichier avec Python. Ici nous allons lire et écrire un fichier  directement dans python avec eux fonctions très simplifiées
```
def read_file(file_name):
  '''lire un fichier'''
  with open(file_name, "r") as f:
    data = f.read()
    return data

def write_file(filename, data):
  '''ecrire un fichier'''
  with open(file_name, "w") as f:
    f.write(data)
    return file_name

```
ici l'idée est de stocker quelquepart le texte issu de la lecture du document.
Commençons par stocker nos deux déclarations dans deux variables d_1789 et d_1948.


* le `formatage` et le nettoyage: nettoyer et convertir pour s'assurer que le texte a une forme manipulable facilement et transférable selon un standard.
On utilise pour cela les méthodes propres au texte, ou liste et aussi un langage/notation/racourci pour détecter des motifs dans le but de produire un texte dans un format particulier et détecter ce qui nous intéresse qu'on appelle regex => **Regex** , la voie "royale"?.

Dans un premier temps nous allons essayer de convertir nos deux déclarations en deux csv dans deux fichiers a part ".csv".

Un csv est un format de fichier standard très utilisé (COMA SEPARATED VALUE), un tableau qui constite dans des lignes ou chaque cellule est séparée par une virgule ",".
La première ligne correspond généralement à l'entête de notre tableau avec le nom des champs.
Il suffit donc de préparer une liste de lignes dont chaque champs est séparé par une virgule.
Comme on stocke du texte qui potentiellement a des virgules on va utilise une tabulation notée "\t" on parle alors de TSV.

```
def write_tsv(filename, data):
  '''ecrire mes données dans un fichier'''
  with open(file_name, "w") as f:
    #data est une liste de lignes
    head = "champ1,champ2,champ3"
    f.write(head)
    for line in data:
      #on ajoute \n à la fin pour sauter la  ligne
      row = line.join("\t")+"\n"
      f.write(row)
    return file_name

```
Evidemment, il existe un module csv qui fait le boulot à notre place si on est paresseux,
je vous invite à la regarder la [documentation du module CSV](https://docs.python.org/3/library/csv.html)

Exercice : Dans un premier temps essayons de convertir nos deux déclarations en deux csv.
Contiendront comme champ le numéro de l'article, le sous numéro de l'article si besoin, le texte et la longueur de l'article.

* Donnez le nombre d'article et de sous-articles pour chaque déclaration


#### Expressions régulières

Parfois il est plus ardu de récupérer simplement des segments de texte qui nous intéresse simplement avec un seul caractère, on utilise dans ce cas les expressions régulières (normalement on dit rationnelles en francais, mais l'usage (en anglais) est l'usage).

Une  expression regulière représente un motif (sous forme de string) à trouver dans un autre texte.
Les expressions régulières sont un "langage" a part entière avec sa notation (syntaxe),  ses méthodes (grammaire) et ses racourcis.
Les fonctions les plus utilisée sont search et match.

Bonne nouvelle les regex sont utilisés de manière régulière dans plein de langages de programmations!
En python il suffit d'importer le module re dans son script
```
import re

```
Les opérateurs de la syntaxe regex :
. ^ $ * + ?

Les notations spéciales pour un e
{ } [ ] \ | ( )

Les raccourcis:
\d matche tous les caractères décimaux compris [0-9].
\D matche tous les caractères excepté les décimaux compris entre 0-9 soit [^0-9]

\s matche tous les caractères d'espacements soit [ \t\n\r\f\v].
\S matche tous les caratères excepté les caractères d'espacement soit [^ \t\n\r\f\v].
\w matches tous les caractères alphanumerique soit [a-zA-Z0-9_].
\W matches tous les caractères excepté les alphanumeriques soit [^a-zA-Z0-9_].
Les fonctions les plus utilisées sont

- search: re.search(pattern, string, flags=0)
- match: re.match((pattern, string, flags=0)

Plutot que de les passer en revue car ce sujet pourrait fire l'objet d'une session à part entière.
Je vous propose de regarder les premières démonstration qu'en fait [Lucas Willems]
(https://www.lucaswillems.com/fr/articles/25/tutoriel-pour-maitriser-les-expressions-regulieres)
et de plonger dans ce tutoriel en anglais (https://www.tutorialspoint.com/python/python_reg_expressions.htm)

>>> Améliorons maitenant notre function `get_keywords()`
en acceptant uniquement les caractères alphanumériques sans ponctuation et espace
et en filtrant les mots de moins de 4 lettres.

* la `segmentation`, le découpage et la simplification:

segmentation/ tokenisation/ balisage/ stemming
découper le texte en petite unité lexicale ou syntaxique et simplifier les formes:

  - mots clés
Nous l'avons déjà fait avec notre function get_keywords que l'on peut évidemment améliorer encore...
  - stopwords
On peut en effet établir une liste noire de mots qui ne nous intéresse pas et filtrer .

  - ngrams

Pour les ngrams, il s'agit de produire des listes de mots clés par paire, triple, quadruple.
Cette fonction est utile pour détecter les mots composés ou les couples de catégories grammaticales, il est très utilisé en TAL avec des méthodes statistiques qui permettent de déterminer
si le mot est plus utilisé en forme simple ou composée ou qu'il comporte un contexte immédiat de negation par exemple.

>>> Ecrivez une fonction bigrame() qui prend un texte et renvoie les paires de mots
>>> Ecriver une fonction ngram() qui prend un texte et une taille et renvoie un ensemble de mots selon la taille spécifiée.

  - forme simplifiée: stems
L'opération de stemming (radicalisation) consiste à simplifier la forme d'un mot et d'en enlever toutes les variations en se concentrant sur sa forme radicale
Exemple: mange, mangeons, mangera, mangeoire, mangeaille sont réduits à la forme "MANG"
Dans ce cas on utilise des outils externes pour faciliter le travail de radicalisation, ils varient évidemment selon les langues et sont constitués par apprentissage.
=> **NLTK**, la boite à outil en python pour le TAL

* le `filtrage`, l'`étiquetage et la categorisation`:

  - motifs récurrents (patterns)
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
