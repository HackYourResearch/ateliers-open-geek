`Atelier 03`
# A la découverte du TextMining

* Petit rappel: le textmining implique de sortir la pelle, la pioche, les ciseaux le marteau on se concentre sur la forme des mots et non sur le sens. On utilise les règles de morphologie, de grammaire et de syntaxe que l'on peut observer. Les traitements qu'on fait dessus sont des traitements **statistiques** et non pas **sémantiques**.

||LINGUISTIQUE|SEMANTIQUE|
|: | :| :|
|Ce qu'on regarde|**forme**| **sens**|
|Example| invention, inventeur, inventer| exact, vrai, correct
|Détail | pluriel, verbe, adjectifs| synonyme, antonyme|
| Procédé | recherche de motif/règles + enquete statistique | recherche de liens/sens + croisement de données|



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
* changer la casse

lower()
upper()
title()

* remplacer des lettres

texte.replace("world", "everybody")
* le découper avec un séparateur

texte.split(" ")
Comme la string est une liste de caractère on peut aussi utiliser les methodes des listes

listes,boucle, dictionnaires

### Ou trouve t-on du texte?
* input(): lire de données entrées par l'utilisateur
* variable: copier coller un texte
* document: lire un fichier
* base de données: récupérer des données

* Exercice3: Pour un texte donné afficher compter le nombre de mot


* Exercice4: Afficher les lettres de l'alphabet chaque lettre sur une nouvelle ligne

### Textmining: procédure
