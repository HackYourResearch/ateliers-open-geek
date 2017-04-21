
# Introduction
## Rappel 1
Où puis-je trouver les styles CSL dans Zotero ? Localiser le répertoire de données `zotero`, puis répertoire `styles`.

## Rappel 2

Tous les problèmes de mise en forme ne proviennent pas des styles bibliographiques, vérifiez la qualité et la complétude des données de votre bibliothèque Zotero en premier lieu !

## Rappel 3

Le plus difficile n'est pas forcément d'encoder le style, mais de disposer de consignes claires et précises, traduisibles dans un langage informatique.

# Principes généraux de CSL

## Principes du langage XML

### Prologue XML

C'est la première ligne du fichier CSL. Il contient la déclaration XML et spécifie le codage des caractères. Il se présentera ainsi dans la plupart des cas : `<?xml version="1.0" encoding="utf-8"?>`.

### Eléments et hiérarchie

Les éléments sont les blocs de base avec lesquels un fichier XML est construit. Ils peuvent être imbriqués hiérarchiquement : on parle d'éléments **parent** et d'éléments **enfant**. Le premier élément est l'élément **racine** (`style` dans le langage CSL), duquel tous les éléments dépendent. On indente généralement les éléments enfant par des espaces ou des tabulations pour faciliter la compréhension.
Chaque élément est introduit par une balise `<ouvrante>` et clos par une balise `</fermante>`, ou une barre oblique s'il n'a pas de contenu. Toute balise ouverte doit impérativement être fermée.
Ex:

```
<element parent>
      <element enfant/>
</element parent>
```
### Attributs et contenu de l’élément

Un élément peut être qualifié et contenir des informations de deux manières :

 - Soit par du contenu textuel inséré entre la balise ouvrante et la balise fermante, ex:
```
<author>
      <name>Anton Perdoncin</name>
      <email>anton.perdoncin@gmail.com</email>
</author>
```
 - Soit par des attributs. Si l'ordre des attributs importe peu, une valeur doit obligatoirement être renseignée, entre guillemets. Ex :
`<link href="http://traces.revues.org" rel="documentation"/>`


### Echappement
Pour éviter toute ambiguïté dans l'écriture XML, certains caractères significatifs pour la syntaxe XML doivent être substitués par d'autres lorsqu'ils sont utilisés dans un attribut ou dans le contenu textuel d'un élément. Les séquences d'échappement sont les suivantes :
 - `&lt;` pour <
 -  `&gt;` pour >
 -  `&amp;` pour &
 - `&apos;` pour ’
 - `&quot;` pour "
### Commentaires
Des commentaires pour expliciter des choix d'écriture ou clarifier des points peuvent être introduits sous la forme suivante :
`<!-- commentaire libre à rédiger -->`. Ils seront reconnus par les applications utilisant le fichier comme du commentaire et non du code.
### Fichier bien formé et valide
Contrairement à HTML, XML ne pardonne aucune erreur de syntaxe. Toute erreur (oubli d'une balise fermante, échappement incorrect, etc.) empêchera le fichier XML de fonctionner. Il convient donc de s'assurer que le fichier CSL fonctionne correctement en vérifiant qu'il est :
 - ** bien formé**, i. e. qu'il respecte les règles de XML et ne contient pas d'erreur d'encodage,
 - ** valide**, i. e. qu'il est conforme aux règles du schéma CSL, qui décrit tous les éléments CSL, leurs attributs et leurs règles d'utilisation.</br>
Adapté de : Rintze M. Zelle, Primer : An introduction to CSL - XML basics - CC-BY-SA - Disponible sur : <http://docs.citationstyles.org/en/stable/primer.html#xml-basics>
## Le « kit CSL »
 - Spécification CSL : http://docs.citationstyles.org/en/stable/specification.html
 - Correspondance types de documents/champs Zotero/CSL : http://aurimasv.github.io/z2csl/typeMap.xml
 - Encodage HTML de la ponctuation (espaces insécables, tirets demi-cadratins, etc.) :
http://character-code.com/punctuation-html-codes.php et http://www.mus.ulaval.ca/roberge/gdrm/08-codes.htm#espaces_tirets
 - Fichier locale-fr : https://github.com/citation-style-language/locales/blob/master/locales-fr-FR.xml

## Structure générale d’un style CSL
- `style` :  élément racine - précise notamment la version de CSL, le type de style et permet des paramétrage globaux (gestion des noms à particules, de l’indication du nombre de pages, abréviation des prénoms composés) - spécification CSL : <http://docs.citationstyles.org/en/1.0.1/specification.html#the-root-element-cs-style>
- `info` : métadonnées décrivant le style (nom, auteur, etc.) - il faudra notamment modifier les éléments `title` et `id` du style que vous aurez créé à partir d'un autre
- `citation` : décrit la façon dont les appels de citation ou les notes (pour les styles _**note**_) sont formatés - spécification CSL : <http://docs.citationstyles.org/en/stable/specification.html#citation>
- `bibliography` : décrit la façon dont la bibliographie est formatée -  spécification CSL : <http://docs.citationstyles.org/en/stable/specification.html#bibliography>
- `macro` : permet la réutilisation des règles de formatage dans `citation` et `bibliography` et des styles plus compacts - spécification CSL : <http://docs.citationstyles.org/en/stable/specification.html#macro>
- `locale` : permet de spécifier des termes, formats de dates et options de formatage différents de ceux prévus par défaut pour la langue - spécification CSL : <http://docs.citationstyles.org/en/stable/specification.html#locale>
 - `terms` : permet la modification de chaînes de caractères spécifiques (ex. remplacer « edited by » par « ed. by ») - spécification CSL : <http://docs.citationstyles.org/en/stable/specification.html#terms>

## Anatomie des éléments `style` et `info`
- Type de style : l’attribut `class`
- Style agnostique du point de vue de la langue vs. style localisé
- Style dépendant (ex : Loisir et Société / Society and Leisure) vs. style indépendant

## Les principaux types d’éléments
On manipule dans les appels de citation, les notes et la bibliographie des données de nature différente, auxquelles des paramétrages spécifiques peuvent être appliqués. A chaque type de donnée correspond ainsi un type d'élément CSL. D'autres élements, `group` et `choose`, par exemple, sont davantage des éléments de rédaction que de contenu.
- `text` :  le texte à afficher peut être celui d’une `variable`, d’une `macro`, d’un `term` ou d’une `value`
- `date` : date de publication, date de consultation, etc.
- `names`: noms des auteurs, des éditeurs scientifiques, des éditeurs commerciaux, etc.
- `number`: volume, numéro, numéro dans la série, etc.
- `label`: étiquette de certaines données, par exemple page ou p. pour page, vol. ou volume pour volume, sous la dir. de pour l’éditeur scientifique, etc.
- `group`  : simplifie l’écriture d’un style en :
 -  définissant la ponctuation au niveau d’un groupe d’éléments plutôt qu’élément par élément,
  -  conditionnant l’affichage de certaines données à la présence d’autres (exemple : ne pas afficher « accessible sur : » s’il n’y a pas d’URL)
- `choose`: créer des conditions - voir _infra_ les différents types de condition

# Outils d’édition des styles = à compléter
Quand j'ai commencé à faire des photographies, j'ai acheté un appareil argentique entièrement manuel.</br>
Quand j'ai commencé à faire de la couture, j'ai acheté une machine entièrement manuelle.</br>
Quand j'ai commencé à éditer des styles CSL, j'ai utilisé l'éditeur intégré à Zotero.

## http://editor.citationstyles.org
### Rechercher un style à partir d'un exemple
### Editer un style
2 modes d'édition :
- éditeur visuel, sous la forme d'un formulaire
- éditeur de code, avec coloration syntaxique
### Avantages/limites

## Les outils intégrés à Zotero
### 2 outils :
- aperçu des styles
- éditeur de style
### Avantages/limites

## L'éditeur de texte
Quelques exemples d'éditeur :
- NotePad++ (pas Mac)
- TextWrangler (Mac)
- Atom (toutes plateformes)
### Avantages/limites

## Valider son style
http://validator.citationstyles.org/

# Exemples de modification mineures d’un style existant
## Macro simple
Exercice de style _Nature_. </br>
Modifiez le formatage des noms d’auteur pour :
- avoir le prénom en entier,
- relier le nom des deux derniers auteurs par and,
- afficher la mention et al en gras.
## Macro conditionnelle
Exercice de style _Nature_. </br>
Modifiez le formatage des titres d’actes de conférence, pour qu’ils soient :
- affichés entre guillemets.

### Les différents types de condition
Attributs possibles pour les éléments `if` et `else-if`.
NB on peut indiquer plusieurs valeurs, sauf pour l’attribut `desambiguate`.
- `desambiguate="true"`(seule valeur possible de l’attribut) : la condition n’est réalisée que si elle permet de désambiguïser
- `is-numeric="variable"` valeur de l’attribut = variable qui doit avoir un contenu numérique pour que la condition se réalise
- `is-uncertain-date="date"` valeur de l’attribut = date qui doit être incertaine pour que la condition se réalise [NB Zotero ne gère pas les dates incertaines]
- `locator="XXX"`valeur de l’attribut = locator auquel la condition s’applique
- `position="XXX"`  cf. infra, utilisées pour les notes de bas de page ou de fin
- `type="XXX"` valeur de l’attribut = type de document auquel la condition s’applique
- `variable="variable"` valeur de l’attribut = variable dont l’absence ou la présence conditionne la réalisation de la condition
 - `match="any"` = OU = la condition se réalise si au moins un des critères est rempli
ex : `<if type="book thesis"  match="any"> `
la condition se réalise si le document est de type livre OU thèse
 - `match="all"` = ET = la condition se réalise si TOUS les critères sont remplis
 - `match="none" `= NON = la condition se réalise si AUCUN des critères n’est rempli
ex : `<if variable="volume"  match="none">`
la condition se réalise si la variable volume est absente, i. e. si le champ Volume de la notice Zotero est vide

## Elément citation  
A compléter en groupe et à partir de : <http://paris-sorbonne.libguides.com/zotero_styles/citation>

## Elément bibliography  
A compléter en groupe et à partir de :

 <http://paris-sorbonne.libguides.com/zotero_styles/bibliography>

# Organisation d’un travail collaboratif en France pour la création de styles de citation en SHS sur Trello
