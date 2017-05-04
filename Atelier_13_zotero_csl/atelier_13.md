# Introduction

## Rappel 1

Où puis-je trouver les styles CSL dans Zotero ? Localiser le répertoire de données `zotero`, puis répertoire `styles`.

## Rappel 2

Tous les problèmes de mise en forme ne proviennent pas des styles bibliographiques, vérifiez la qualité et la complétude des données de votre bibliothèque Zotero en premier lieu !

## Rappel 3

Le plus difficile n'est pas forcément d'encoder le style, mais de disposer de consignes claires et précises, traduisibles dans un langage informatique.

_==> un exemple à suivre pour les revues, les indications de infoclio pour les règles de citation : [https://www.infoclio.ch/fr/node/139278](https://www.infoclio.ch/fr/node/139278). Cette page précise en outre de façon détaillée les champs Zotero utilisés pour chaque type de document._

# Principes généraux de CSL
## Principes du langage XML
### Prologue XML

C'est la première ligne du fichier CSL. Il contient la déclaration XML et spécifie le codage des caractères. Il se présentera ainsi dans la plupart des cas : `<?xml version="1.0" encoding="utf-8"?>`.

### Eléments et hiérarchie

Les éléments sont les blocs de base avec lesquels un fichier XML est construit. Ils peuvent être imbriqués hiérarchiquement : on parle d'éléments **parent** et d'éléments **enfant**. Le premier élément est l'élément **racine** (`style` dans le langage CSL), duquel tous les éléments dépendent. On indente généralement les éléments enfant par des espaces ou des tabulations pour faciliter la compréhension. Chaque élément est introduit par une balise `<ouvrante>` et clos par une balise `</fermante>`, ou une barre oblique s'il n'a pas de contenu. Toute balise ouverte doit impérativement être fermée. Ex:
```
<element parent>
      <element enfant1 attribut="valeur"/>
      <element enfant2> text </element enfant2>
</element parent>
```

_==> ici il faut comprendre que l'élément enfant 1 est qualifié par un attribut et que le contenu de l'élement enfant 2 est du texte, entre deux balises (cf. ci-dessous)_

### Attributs et contenu de l’élément

Un élément peut être qualifié et contenir des informations de deux manières :

*   Soit par du contenu textuel inséré entre la balise ouvrante et la balise fermante, ex:

```
<author>
   <name>Anton Perdoncin</name>
   <email>anton.perdoncin@gmail.com</email>
</author>
```

*   Soit par des attributs. Si l'ordre des attributs importe peu, une valeur doit obligatoirement être renseignée, entre guillemets. Ex : `<link href="http://traces.revues.org" rel="documentation"/>`

### Echappement

Pour éviter toute ambiguïté dans l'écriture XML, certains caractères significatifs pour la syntaxe XML doivent être substitués par d'autres lorsqu'ils sont utilisés dans un attribut ou dans le contenu textuel d'un élément. Les séquences d'échappement sont les suivantes :

*   `&lt;` pour <
*   `&gt;` pour >
*   `&amp;` pour &
*   `&apos;` pour ’
*   `&quot;` pour "

### Commentaires

Des commentaires pour expliciter des choix d'écriture ou clarifier des points peuvent être introduits sous la forme suivante : `<!-- commentaire libre à rédiger -->`. Ils seront reconnus par les applications utilisant le fichier comme du commentaire et non du code.

### Fichier bien formé et valide

Contrairement à HTML, XML ne pardonne aucune erreur de syntaxe. Toute erreur (oubli d'une balise fermante, échappement incorrect, etc.) empêchera le fichier XML de fonctionner. Il convient donc de s'assurer que le fichier CSL fonctionne correctement en vérifiant qu'il est :

*   **bien formé**, _i. e._ qu'il respecte les règles de XML et ne contient pas d'erreur d'encodage,
*   **valide**, _i. e._ qu'il est conforme aux règles du schéma CSL, qui décrit tous les éléments CSL, leurs attributs et leurs règles d'utilisation.
    Adapté de : Rintze M. Zelle, Primer : An introduction to CSL - XML basics - CC-BY-SA - Disponible sur : [http://docs.citationstyles.org/en/stable/primer.html#xml-basics](http://docs.citationstyles.org/en/stable/primer.html#xml-basics)

## Le « kit CSL »

### Spécification CSL

[http://docs.citationstyles.org/en/stable/specification.html](http://docs.citationstyles.org/en/stable/specification.html)

_==> Le Dictionnaire et la grammaire de CSL_

### Correspondance types de documents/champs Zotero/CSL

[http://aurimasv.github.io/z2csl/typeMap.xml](http://aurimasv.github.io/z2csl/typeMap.xml)

_==> Spécificités de Zotero : exemple la date originale est une varaiable CSL mais ne correspond pas à un champ Zotero. Il faut donc utiliser de façon spécifique le champ `Extra` pour renseigner une date originale (de même qu'un éditeur et un lieu de publication originaux)._

*   Date originale d’un document = 1 variable de type date = `original-date`
*   Lieu de publication original d’un document = `original-publisher-place`
*   Editeur original d’un document = `original-publisher`.

Ex encodage CSL : `<date variable="original-date" form="text" date-part="year"/>` Ces variables doivent être saisies dans le champ `Extra` de la notice Zotero, sous la forme :
```
{:original-date: 1891}
{:original-publisher: Librairie Ch. Delagrave}
{:original-publisher-place: Paris}
```
 On peut aussi détourner des champs, mais cela doit être fait avec prudence :
    *   tous les champs ne sont pas disponibles pour tous les types de documents ;
    *   on risque de se priver d'un champ utile pour certains types de document ;
    *   il faut bien indiquer à tous les utilisateurs du style le détournement effectué.

### Encodage HTML de la ponctuation (espaces insécables, tirets demi-cadratins, etc.)

[http://character-code.com/punctuation-html-codes.php](http://character-code.com/punctuation-html-codes.php) et [http://www.mus.ulaval.ca/roberge/gdrm/08-codes.htm#espaces_tirets](http://www.mus.ulaval.ca/roberge/gdrm/08-codes.htm#espaces_tirets)

_==> Spécificités françaises à encoder_

### Fichier locale-fr

[https://github.com/citation-style-language/locales/blob/master/locales-fr-FR.xml](https://github.com/citation-style-language/locales/blob/master/locales-fr-FR.xml)

_==> Éléments de traduction en français : traduction par défaut disponible_

## Structure générale d’un style CSL

*   `style` : élément racine - précise notamment la version de CSL, le type de style et permet des paramétrages globaux : gestion des noms à particules avec l'attribut `demote-non-dropping`, de l’indication du nombre de pages, abréviation des prénoms composés - spécification CSL : [http://docs.citationstyles.org/en/1.0.1/specification.html#the-root-element-cs-style](http://docs.citationstyles.org/en/1.0.1/specification.html#the-root-element-cs-style)

_==> Certains styles sont agnostiques du point de vue de la langue, ils ne comportent pas d'attribut `default-locale`. Ils peuvent être utilisés dans toutes les langues ; ce sont alors les paramètres par défaut définis dans les fichiers `locale` qui sont appliqués (voir lien vers le fichier `locale-fr-FR` dans le kit CSL). Certains styles sont quant à eux utilisables pour certaines langues seulement, ce qui permet de définir des spécificités propres à la langue différentes de celles prévues par défaut (en termes de ponctuation, de termes prédéfinis, etc.). Dans l'entrepôt des styles Zotero on peut retrouver les styles localisés dans une langue en indiquant le nom de la langue dans le formulaire de recherche : "french" affichera ainsi tous les styles ayant un attribut `default-locale="fr-XX"`._

*   `info` : métadonnées décrivant le style (nom, auteur, etc.) - il faudra notamment modifier les éléments `title` et `id` du style que vous aurez créé à partir d'un autre

_==> il faut bien changer l'`id` et le `title` sinon le style que vous avez créé sera écrasé lors des mises à jour du style duquel il est dérivé._

*   `citation` : décrit la façon dont les appels de citation ou les notes (pour les styles _**note**_) sont formatés - spécification CSL : [http://docs.citationstyles.org/en/stable/specification.html#citation](http://docs.citationstyles.org/en/stable/specification.html#citation)

*   `bibliography` : décrit la façon dont la bibliographie est formatée - spécification CSL : [http://docs.citationstyles.org/en/stable/specification.html#bibliography](http://docs.citationstyles.org/en/stable/specification.html#bibliography)

*   `macro` : permet la réutilisation des règles de formatage dans `citation` et `bibliography` et des styles plus compacts - spécification CSL : [http://docs.citationstyles.org/en/stable/specification.html#macro](http://docs.citationstyles.org/en/stable/specification.html#macro)

_==> Une macro est un programme qui permet d'être appelé (fonction), il est plus facile de faire des macro pour que ça soit plus propre. C'est aussi ce qu'on utilise pour faire des mises en forme conditionnelles. C'est l'une des bonnes pratiques d'écriture recommandées par adamsmith : Bonne pratique 2 : Utilisez abondamment les macros. Gardez les éléments `citation` et `bibliography` brefs et ne leur intégrez qu'au minimum des éléments `choose`." Source : Adamsmith. Writing CSL - Features and Best Practices. The Zoteroist, 2013\. Disponible sur : [https://zoteromusings.wordpress.com/2013/10/28/writing-csl-features-and-best-practices](https://zoteromusings.wordpress.com/2013/10/28/writing-csl-features-and-best-practices)"_

*   `locale` : permet de spécifier des termes, formats de dates et options de formatage différents de ceux prévus par défaut pour la langue - spécification CSL : [http://docs.citationstyles.org/en/stable/specification.html#locale](http://docs.citationstyles.org/en/stable/specification.html#locale)

*   `terms` : permet la modification de chaînes de caractères spécifiques (ex. remplacer « edited by » par « ed. by ») - spécification CSL : [http://docs.citationstyles.org/en/stable/specification.html#terms](http://docs.citationstyles.org/en/stable/specification.html#terms) - voir aussi : [https://zoteromusings.wordpress.com/2013/10/28/writing-csl-features-and-best-practices](https://zoteromusings.wordpress.com/2013/10/28/writing-csl-features-and-best-practices)

## Anatomie des éléments `style` et `info`

*   Type de style : l’attribut `class`
*   Style agnostique du point de vue de la langue vs. style localisé
*   Style dépendant (ex : Loisir et Société / Society and Leisure) vs. style indépendant.

_==> Pour économiser du code, certains styles sont dépendants d'un autre style. Dans ce cas là, le fichier CSL se réduit à un élément info. La référence au style principal est indiquée par l'attribut_
 `rel="independent-parent"`.
```
<?xml version="1.0" encoding="utf-8"?>
<style xmlns="http://purl.org/net/xbiblio/csl" version="1.0" default-locale="en-US">
  <!-- Generated with https://github.com/citation-style-language/utilities/tree/master/generate_dependent_styles/data/taylor-and-francis -->
  <info>
    <title>Loisir et Société / Society and Leisure</title>
    <id>http://www.zotero.org/styles/loisir-et-societe-society-and-leisure</id>
    <link href="http://www.zotero.org/styles/loisir-et-societe-society-and-leisure" rel="self"/>
    <link href="http://www.zotero.org/styles/apa" rel="independent-parent"/>
    <link href="http://www.tandfonline.com/action/authorSubmission?journalCode=RLES20&amp;page=instructions" rel="documentation"/>
    <category citation-format="author-date"/>
    <category field="political_science"/>
    <issn>0705-3436</issn>
    <eissn>1705-0154</eissn>
    <updated>2014-05-17T16:39:46+00:00</updated>
    <rights license="http://creativecommons.org/licenses/by-sa/3.0/">This work is licensed under a Creative Commons Attribution-ShareAlike 3.0 License</rights>
  </info>
</style>
```
## Les principaux types d’éléments

On manipule dans les appels de citation, les notes et la bibliographie des données de nature différente, auxquelles des paramétrages spécifiques peuvent être appliqués. A chaque type de donnée correspond ainsi un type d'éléments CSL. D'autres élements, `group` et `choose`, par exemple, sont davantage des éléments de rédaction que de contenu.

*   `text` : le texte à afficher peut être celui d’une `variable`, d’une `macro`, d’un `term` ou d’une `value`

*   `date` : date de publication, date de consultation, etc.

*   `names`: noms des auteurs, des éditeurs scientifiques, des éditeurs commerciaux, etc.

*   `number`: volume, numéro, numéro dans la série, etc.

*   `label`: étiquette de certaines données, par exemple page ou p. pour page, vol. ou volume pour volume, sous la dir. de pour l’éditeur scientifique, etc.

*   `group` : simplifie l’écriture d’un style en :

    *   définissant la ponctuation au niveau d’un groupe d’éléments plutôt qu’élément par élément,
    *   conditionnant l’affichage de certaines données à la présence d’autres (voir exemple : [https://zoteromusings.wordpress.com/2013/10/28/writing-csl-features-and-best-practices/](https://zoteromusings.wordpress.com/2013/10/28/writing-csl-features-and-best-practices/)
*   `choose`: créer des conditions - voir _infra_ les différents types de condition

# Outils d’édition des styles

Quand j'ai commencé à faire des photographies, j'ai acheté un appareil argentique entièrement manuel.

Quand j'ai commencé à faire de la couture, j'ai acheté une machine entièrement manuelle.

Quand j'ai commencé à éditer des styles CSL, j'ai utilisé l'éditeur intégré à Zotero.

## Editeur de style Zotero

_==> Aller dans Zotero >Préférences > Avancées > Générales > Ouvrir Editeur de style_

_On sélectionne le style, des documents de sa bibliothèque, puis on actualise pour afficher la fenêtre de code et la prévisualisation des citations et de la bibliographie._

### Avantages

*   Toute erreur de syntaxe XML donne lieu à un message d'erreur immédiat : on voit tout de suite que son fichier n'est pas bien formé.
*   On prévisualise en direct les modifications de paramétrage du style, et ce à partir des exemples de document de sa bibliothèque.

### Limites

*   Pas de coloration syntaxique
*   Pas de contrôle de la validité CSL
*   L'écran est découpé en 3 bandeaux horizontaux, ce qui peut occasionner une lisibilité très réduite en fonction de la taille de son écran

## Editeur de style en ligne

[http://editor.citationstyles.org](http://editor.citationstyles.org)

### Rechercher un style à partir d'un exemple

### Editer un style

2 modes d'édition :

*   éditeur visuel, sous la forme d'un formulaire
*   éditeur de code, avec coloration syntaxique

### Avantages

*   Coloration syntaxique
*   Toute erreur de syntaxe XML donne lieu à un message d'erreur immédiat : on voit tout de suite que son fichier n'est pas bien formé
*   Pas de contrôle de la validité CSL
*   Prévisualisation en direct des modifications de paramétrage du style

### Limites

*   La prévisualisation n'est pas effectuée à partir des documents de sa bibliothèque, elle porte uniquement sur des exemples non personnalisables de livre et d'article

## L'éditeur de texte

Quelques exemples d'éditeur :

*   NotePad++ (pas Mac)
*   TextWrangler (Mac)
*   Atom (toutes plateformes)

### Avantages

*   Coloration syntaxique
*   Contrôle de la validité CSL si on utilise un éditeur XML
*   En fonction de l'éditeur, aides à la saisie et contrôle du caractère bien formé du fichier

### Limites

*   Pas de prévisualsation des modifications de paramétrage du style

## Valider son style

Cet outil permet de vérifier que son fichier CSL respecte bien le langage CSL et est valide. NB un fichier peut être bien formé, respecter la syntaxe XML (balises ouvertes bien fermées, etc.) et ne pas être valide par rapport au schéma CSL. Or cette validité est indispensable pour installer le fichier CSL dans Zotero et pouvoir l'utiliser. [http://validator.citationstyles.org/](http://validator.citationstyles.org/) permet de valider son fichier et affiche le cas échéant de façon détaillée les erreurs d'encodage.

# Exemples de modification mineures d’un style existant

## Macro simple

Exercice de style _Nature_.

**Exemple de la macro auteur** Exemple commenté avec capture d'écran ici : [https://paris-sorbonne.libguides.com/zotero_styles/macros](https://paris-sorbonne.libguides.com/zotero_styles/macros)

Modifiez le formatage des noms d’auteur pour :

*   avoir le prénom en entier;
*   relier le nom des deux derniers auteurs par and ;
*   afficher la mention et al en gras.

_==> aller dans la macro `author`. Faire bien attention à la ponctuation, il faut indiquer explicitement les espaces après les marques de ponctuation_

_Avant_
```
<macro name="author">
    <names variable="author">
      <name sort-separator=", " delimiter=", " and="symbol" initialize-with=". " delimiter-precedes-last="never" name-as-sort-order="all"/>
      <label form="short" prefix=", "/>
      <et-al font-style="italic"/>
    </names>
  </macro>
```
_Après_
```
<macro name="author">
    <names variable="author">
      <name sort-separator=", " delimiter=", " and="text" delimiter-precedes-last="never" name-as-sort-order="all"/>
      <label form="short" prefix=", "/>
      <et-al font-weight="bold"/>
    </names>
  </macro>
  ```

==> On peut aussi changer le

*   `delimiter` par exemple une ,
*   `name-as-sort-order` : all on a toujours Nom-Prénom, Nom-Prénom etc.,
*   `et-al` si on le veut en italique ou en gras `font-style ="italic"` ou `font-weight="bold"`. On peut aller voir la documentation csl en recherchant l'attribut pour voir les valeurs possibles.

**Autre exemple :**

*   pour le nom d'auteur en majuscule
```
<names variable="author">
      <name sort-separator=" " name-as-sort-order="all" et-al-min="4" et-al-use-first="3">
        <name-part name="family" font-variant="small-caps"/>
      </name>
      ...
```

## Macro conditionnelle

_==> ce sont des macros plus complexes où on peut utiliser `<choose>` pour définir des conditions._

### Les différents types de condition

Attributs possibles pour les éléments `if` et `else-if`. NB on peut indiquer plusieurs valeurs, sauf pour l’attribut `desambiguate`.

*   `desambiguate="true"`(seule valeur possible de l’attribut) : la condition n’est réalisée que si elle permet de désambiguïser
*   `is-numeric="variable"` valeur de l’attribut = variable qui doit avoir un contenu numérique pour que la condition se réalise
*   `is-uncertain-date="date"` valeur de l’attribut = date qui doit être incertaine pour que la condition se réalise [NB Zotero ne gère pas les dates incertaines]
*   `locator="XXX"`valeur de l’attribut = locator auquel la condition s’applique
*   `position="XXX"` cf. infra, utilisées pour les notes de bas de page ou de fin
*   `type="XXX"` valeur de l’attribut = type de document auquel la condition s’applique
*   `variable="variable"` valeur de l’attribut = variable dont l’absence ou la présence conditionne la réalisation de la condition
    *   `match="any"` = OU = la condition se réalise si au moins un des critères est rempli ex : `<if type="book thesis" match="any">` la condition se réalise si le document est de type livre OU thèse
    *   `match="all"` = ET = la condition se réalise si TOUS les critères sont remplis
    *   `match="none"`= NON = la condition se réalise si AUCUN des critères n’est rempli ex : `<if variable="volume" match="none">` la condition se réalise si la variable volume est absente, i. e. si le champ Volume de la notice Zotero est vide


**Exercice de style _Nature_.**

Exemple commenté avec capture d'écran ici : [https://paris-sorbonne.libguides.com/zotero_styles/macros](https://paris-sorbonne.libguides.com/zotero_styles/macros).
- Modifiez le formatage des titres d’actes de conférence, pour qu’ils soient affichés entre guillemets.

_Avant_
```
<macro name="title">
    <choose>
      <if type="bill book graphic legal_case legislation motion_picture report song" match="any">
        <text variable="title" font-style="italic"/>
      </if>
      <else-if type="chapter" match="any"/>
      <else>
        <text variable="title"/>
      </else>
    </choose>
  </macro>
```

_Après_

```
<macro name="title">
    <choose>
      <if type="bill book graphic legal_case legislation motion_picture report song" match="any">
        <text variable="title" font-style="italic"/>
      </if>
      <else-if type="chapter" match="any"/>
      <else-if type="paper-conference" match="any">
        <text variable="title" quotes="true"/>
      </else-if>
      <else>
        <text variable="title"/>
      </else>
    </choose>
  </macro>
```

_==>NB le `title` correspond au titre du document. Si on souhaite définir le formatage du titre de revue (pour les articles), du titre de livre (pour les chapiters), du titre des actes (pour les conférences), il faut utiliser la variable `container-title`._

```
<macro name="container-title">
   <choose>
     <if type="article-journal">
       <text variable="container-title" font-style="italic" form="short"/>
     </if>
     <else>
       <text variable="container-title" font-style="italic"/>
     </else>
   </choose>
 </macro>
```

## Elément citation

Exemples commentés et détails ici : [http://paris-sorbonne.libguides.com/zotero_styles/citation](http://paris-sorbonne.libguides.com/zotero_styles/citation)

**Exemple style numérique**

```
<citation collapse="citation-number">
    <sort>
      <key variable="citation-number"/>
    </sort>
    <layout vertical-align="sup" delimiter=",">
      <text variable="citation-number"/>
    </layout>
  </citation>
```

_==> `sort` indique l'ordre (numérique ou bien chronologique ou par nom d'auteur), `layout` nous montre le rendu. Il y a des paramètres particuliers pour les styles auteur-date, notamment pour désambiguïser les appels de citation (documents distincts ayant le même premier auteur et la même date de publication). Pour les styles note, c'est dans cet élément que l'on configure les notes, avec des paramètres particuliers pour gérer les op. cit., etc._

**Exemple style auteur-date**

```
<citation et-al-min="4" et-al-use-first="1" disambiguate-add-year-suffix="true" disambiguate-add-names="true" disambiguate-add-givenname="true" collapse="year" >
    <sort>
      <key macro="author-short"/>
       <key macro="year-date"/>
    </sort>
    <layout prefix=" (" suffix=")" delimiter="&#160;; ">
      <group delimiter=", ">      
            <group delimiter=" ">
                    <text macro="author-short"/>
                    <text macro="year-date"/>
             </group>
            <group>
              <label variable="locator" suffix=".&#160;" form="short"/>
              <text variable="locator"/>
           </group>
    </group>
  </layout>
  </citation>
```
**Exemple style note**
```
<citation et-al-min="4" et-al-use-first="1" disambiguate-add-year-suffix="true" disambiguate-add-names="true" disambiguate-add-givenname="true" givenname-disambiguation-rule="primary-name">
    <layout prefix="&#160;(" suffix=")" delimiter="; ">
      <choose>
        <if position="ibid-with-locator">
          <group delimiter=", ">
            <text term="ibid" text-case="capitalize-first" font-style="italic" suffix="."/>
            <text variable="locator" prefix="p. "/>
          </group>
        </if>
        <else-if position="ibid">
          <text term="ibid" text-case="capitalize-first" font-style="italic"/>
        </else-if>
        <else>
          <group delimiter=" ">
            <text macro="contrib-court"/>
            <text macro="year-short"/>
          </group>
          <group prefix=", ">
            <label variable="locator" form="short" suffix="&#160;"/>
            <text variable="locator"/>
          </group>
        </else>
      </choose>
    </layout>
  </citation>
```
## Elément bibliography

Exemples commentés et détails ici : [http://paris-sorbonne.libguides.com/zotero_styles/bibliography](http://paris-sorbonne.libguides.com/zotero_styles/bibliography)

**Un exemple :**
```
<bibliography et-al-min="6" et-al-use-first="1" second-field-align="flush" entry-spacing="0" line-spacing="2">
    <layout>
      <text variable="citation-number" suffix="."/>
      <group delimiter=" ">
        <text macro="author" suffix="."/>
        <text macro="title" suffix="."/>
        <choose>
          <if type="chapter paper-conference" match="any">
            <text term="in" form="long" plural="false"/>
          </if>
        </choose>
        <text macro="container-title"/>
        <text macro="editor"/>
        <group font-weight="bold">
          <text variable="volume" suffix=","/>
        </group>
        <text variable="page"/>
        <text macro="issuance"/>
        <text macro="access"/>
      </group>
    </layout>
  </bibliography>
  ```
==> Ce sont ainsi des attributs de l'élément `bibliography` qui permettent de paramétrer notamment :

- le nombre d'auteur avant l'indication d'un al `et-al-min="6"`,
- `second-field-align="flush"` pour le retrait de seconde ligne.

## Enregistrer son style

_==> Pour enregistrer son style : dans l'éditeur Zotero, pensez à bien changer le nom du titre et l'identifiant et faire 'enregistrer sous' pour générer le fichier CSL. Pour l'installer : soit on le fait glisser dans une fenêtre de Firefox, soit on va dans Zotero > Préférences > Citer > Gestionnaire de style et on peut rajouter ou supprimer des styles Pour Standalone, voir aussi : https://www.zotero.org/support/styles_Pour éviter les mauvaises surprises à cette ultime étape, n'oubliez pas de valider au préalable votre style grâce au validateur en ligne : http://validator.citationstyles.org/._

# Organisation d’un travail collaboratif en France pour la création de styles de citation en SHS sur Trello

Allez sur : [https://trello.com/b/ACMPVFQf/csl-france](https://trello.com/b/ACMPVFQf/csl-france)

Organisation du trello :

*   style demandés
*   style en cours de création
*   styles prêts à l'usage


# Questions fin de séance

*   utiliser bien le forum Zotero pour poser ces questions (le forum est très réactif et souvent on a des réponses aux questiosn que d'autres se sont déjà posées)

*   pour d'autres langues : Juris-M permet de gérer le multilinguisme

*   utilisation de CSL : par Mendeley, Papers,

*   lien avec LaTex : l'une des meilleures solutions jusqu'à présent était Better Bib(La)Tex, mais pour l'instant sa compatibilité avec Zotero v5 n'est pas assurée.

Document réalisé par Frédérique Flamerie (Blog Zotero Francophone)
