# Atelier #1 - Introduction au cycle - exemple de Markdown

## Premiers pas

Beaucoup de langages informatiques, dont le markdown, font appel à des
caractères par forcément habituels et qui sont parfois difficiles à trouver
sur un clavier.

### Mac - clavier AZERTY

- [ et ] : Alt-Shift-( et Alt-Shift-)
- { et } : Alt-( et Alt-)

## Le langage Markdown

### Présentation

Le langage [Markdown](http://daringfireball.net)  est une sorte de langage informatique permettant une prise de note naturelle et puissante sans dépendre de logiciels complexes et ne nécessitant pas un apprentissage fastidieux.

Au contraire du HTML, le langage qui permet l'écriture des pages web et qui permet de créer d'élégants affichages, le langage Markdown propose une syntaxe plus simple, facilement transformable en page web élégante.

Par exemple, la mise en *italique* d'un mot en html se fera de la manière suivante :

    <em>exemple</em>

Tandis qu'en Markdown, on écrira plus simplement :

    *exemple*

C'est une excellente alternative à Microsoft Word pour la prise de note et même l'écriture de documents plus importants (e.g. écriture d'article avec citation de références bibliographiques : [Scholarly Markdown](http://blog.martinfenner.org/2013/06/17/what-is-scholarly-markdown/)).

### Logiciels d'édition Markdown

#### En ligne

Il existe des éditeurs Markdown en ligne (prendre bien garde à sauvegarder, en local, le document rédigé):

- http://markable.in/editor/
- http://dillinger.io/

#### Toutes plateformes

- Atom.io

#### Mac

Sur Mac, l'application [Mou](http://25.io/mou/) est fortement recommandée car elle autorise l'édition Markdown tout en ayant un aperçu du résultat final en temps réel.


### Premiers pas

Pour un résumé en français des commandes de base, il y a un [excellent tutoriel sur OpenClassRooms](http://fr.openclassrooms.com/informatique/cours/redigez-en-markdown) résumé ci-dessous :

- Titres
    + Premier niveau : `# Mon titre`
    + Deuxième niveau : `## Mon sous-titre`
    + Troisième niveau : `### Mon sous-sous titre`
    + etc.
- Mise en forme
    + Italique : `*mon texte*`
    + Gras : `**mon texte**`
- Liste : 
    ```Markdown
    - Élément de premier niveau
        - Élément de second niveau
        - Élément de second niveau

    Il est possible de varier les caractères utilisés comme puce,
    pour améliorer la lisibilité, par exemple :

    - Élément de premier niveau
        * Élément de second niveau
            + Élément de troisième niveau

    On peut aussi réaliser des listes numérotées :

    1. Élément 1
    2. Élément 2
    3. etc.
    ```
- Lien `[Titre du lien](http://monlien.com)`
- etc. (citations, extraits de code source, images, ligne de séparation, tableaux ...)
