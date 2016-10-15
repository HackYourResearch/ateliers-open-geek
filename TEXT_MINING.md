`Atelier 03`
# A la découverte du TextMining





## Qu'est ce qu'un texte en Python?
    C'est un `type de données` qu'on appelle `string`
Un ensemble de caractères stockés les uns à la suite des autres qui donne une chaine de caractères

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
Comme ce sont des caractères les uns à la suite des autres, le texte est stocké de la même manière qu'une `liste`
pour savoir combien de lettres dans ma phrase
```
>>> print len(salut)
10
>>>
```
Attention l'espace compte pour un caractère car c'est un caractère.

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
* Exercice0: Le traditionnel hello world
* Exercice1: Afficher les lettres de l'alphabet
* Exerice2: Afficher les lettres de l'alphabet à l'envers
* Exercice 4: Afficher les 4 dernières lettres de l'alphabet dans l'ordre inversé
##### Manipulation du texte string
String est un type de données et lui sont attachées un ensemble de méthodes propres
* on peut les unir ensemble +
* les multiplier * 3
* changer la casse:

lower()
upper()
title()

* remplacer des lettres

texte.replace("world", "everybody")
* le découper avec un séparateur
texte.split(" ")

Comme la string est une `liste` de caractère on peut aussi utiliser les methodes des listes

listes,boucle, dictionnaires

### Ou trouve t-on du texte?
* input(): lire de données entrées par l'utilisateur
* variable: copier coller un texte
* document: lire un fichier
* base de données: récupérer des données par requete et Croisement
* web, mail, logs

* Exercice 3: Pour un texte donné afficher compter le nombre de mot


* Exercice 4: Afficher les lettres de l'alphabet chaque lettre sur une nouvelle ligne

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

Les principales étapes pour une enquête sur un corpus de données textuelles sont:

* le `parsing` lecture et sauvegarde: soit parcourir et enregister le texte de manière à ce qu'on puisse facilement y accéder

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
* Anlayse de sentiment
