# Retour sur les Bases

## Histoire de l'informatique
À la racine de l'informatique se trouve la volonté d'automatiser.
Automatiser, c'est faire faire à la machine les tâches répétitives, où l'humain est bien moins efficace que la machine, pour le laisser se concentrer sur des tâches plus complexes.

Aux premiers pas de l'automatisation, on trouve les automates, sortes de robots mécaniques.
Il faut noter qu'aux tout débuts de l'automatisation, et avant son utilisation massive dans l'industrie, on réalisait surtout des automates à des fins d'amusement et le divertissement.

On peut voir un automate comme un ensemble d'états et des règles de transition entre les états.

Par exemple : Les fantômes de PacMan commencent leur vie en chassant PacMan (état 1) et se mettent à le fuire (état 2) quand PacMan mange un point blanc (transition).

L'avantage de l'ordinateur sur l'automate mécanique, est la possibilité de créer "facilement" + d'états et + de transition, tout en étant à même de les modifier après coup.

Basiquement, la base dun ordinateur est une machine à registre, c'est à dire une machine possédant des "récipients", contenant des "objets" et étant capable de faire des opérations sur ces récipients et ces objets : enlever un objet d'un récipient, ajouter un objet à un récipient, vérifier si un objet est vide ...

Toutes ces choses simples permettent de faire les opérations logiques qui permettent ensuite d'ouvrir la porte à tous les besoins en automatisation qu'on a.
C'est ce qu'a démontré Turing, en définissant l'ensemble d'opération minimal qui permettait de "tout" faire.

Ce "tout" est toutefois limité par le nombre de registre et leur taille. Un ordinateur avec une infinité de registres de taille infinie est donc en théorie capable de réaliser n'importe quelle opération.

Pour aller plus loin que ces "opérations minimales", on défini, dans un ordinateur, des registres spéciaux, qui vont, lorsqu'ils sont utilisés, réaliser un ensemble d'opérations données. On dit qu'on rajoute de l'abstraction.

On parle de "niveaux d'abstraction" ou de "couches d'abstraction" pour d'écrire la superposition de tels registres, groupant des opérations afin de faciliter la vie à l'utilisateur.

Ainsi, on trouve les opérations de Turing sur la première couche, puis on va trouver des langages un peu plus complexes, comme l'assembleur, quelques couches plus haut, puis des langages comme Python sur des couches encore supérieures et les fenêtres d'interface tout en haut.

Au coeur des ordinateurs modernes, on trouve ces registres dans ce qu'on appel la **mémoire**. Et les opérations sur ces registres sont réalisées par le **processeur**.

## Votre Ordinateur

### Le matériel
le **processeur** manipule des 0 et des 1 écrits en mémoire en suivant une instruction.

La **mémoire** de votre ordinateur peut être de différents types et se trouver sur différents supports.

Comme le cerveau humain, certaines mémoires à long terme sont stables dans le temps mais sont un peu plus lentes que des mémoires plus rapides mais ayant une durée de vie limitée.

 - la mémoire vive est une mémoire rapide, de travail, mais  dont l'information s'efface quand on coupe le courant
 - le disque dur est une mémoire à long terme, où l'information reste tant qu'on ne la re-modifie pas

Les **langages** informatiques sont les "couches d'abstractions" qui permettent d'écrire des instructions de façon un peu moins pénible qu'avec des suites de 0 et de 1 :

 - [cartes perforées](http://fr.wikipedia.org/wiki/Carte_perfor%C3%A9e) (soyez heureux d'avoir un clavier au lieu d'une poinçonneuse !)
 - (explosion de langages pour des usages plus ou moins spécifiques)
 - Ceux que vous verrez dans ces ateliers :
 
   -  MarkDown
   -  [Python](https://www.python.org/)
   -  [R](http://cran.r-project.org/)

### La ligne de commande
C'est l'interface privilégiée avec l'ordinateur quand on veut le soumettre à notre volonté.
Elle utilise un langage qui permet de communiquer avec l'ordinateur (de façon assez frustre, entendons-nous) c'est-à-dire d'envoyer des instructions à l'ordinateur et de voir l'output de ces instructions s'afficher à l'écran.


système|nom|pour ouvrir|langage
-------|--------|--------|------
windows|fenêtre de commande,... |win+R puis cmd| dos
mac|terminal,iterm,...|/Applications/Utilities/Terminal| bash
linux|terminal emulator,xterm,...|se loguer|bash, tcsh,...

`Ouvrez une fenêtre de commande. Quelles sont les informations affichées automatiquement?`

### L'arborescence des fichiers
C'est une façon de se représenter et d'organiser l'information stockée sur le disque dur  
**Il vaut mieux toujours savoir où on est dans cette arborescence !**
  
**Concepts clef** :

- racine : c'est le point de départ de l'organisation des informations (particularité de windows : il peut y en avoir plusieurs)
- repertoire : c'est un contenant qui peut contenir des fichiers ou d'autres répertoires
- fichier : en simplifiant ça correspond à une zone de mémoire où sont stockées des informations (texte,video,données, script,...)
- chemin (ou _path_) : c'est la description de là où se trouve un répertoire ou un fichier en partant de la racine
- répertoire courant : c'est l'endroit où on se trouve à un instant donné dans l'arborescence, c'est là qu'on cherchera à ouvrir ou à écrire un fichier si on ne précise rien de plus
- chemin relatif : le chemin à partir du répertoire courant

**Remarques** :

- on peut éditer des fichiers mais généralement pas des répertoires !
- les fichiers et les répertoires comportent des méta-données (comme vos photos,emails,...) qui disent qui a le droit de faire quoi avec
- oui je sais techniquement un répertoire c'est aussi un fichier (c'est de l'info en la mémoire) mais pas la peine de s'embrouiller.

**Pour aller plus loin**
Les systèmes de fichiers, avec des fonctionnalités différentes et malheureusement pas forcément compatibles les uns avec les autres, correspondent à la manière de transcrire physiquement sur la mémoire cette structure.
Exemples :

- FAT 32, File Allocation Table depuis windows 95 : limite la taille des fichiers à 4 Go, le seul système de fichier bien supporté par tous les systèmes d'exploitation
- NTFS, New Technology File System : depuis Windows NT, nécessite des ajouts logiciels pour être plus ou moins supporté sous mac
- exFAT, Extended File Allocation Table : Windows, à éviter comme la peste
- ext, extended file system : linux, actuellement en version ext4
- HFS et HFS+, Hierarchical File System : mac avec une taille minimale de fichier qui gaspille de l'espace


**Afficher le nom, le contenu et changer de répertoire courant**

langage|nom|contenu|changer
-------|--------|--------|--
dos|chdir|dir|chdir
bash|pwd|ls|cd
python module os|os.getcwd()|os.listdir()|os.chdir

`Essayez ces manipulations en ligne de commande avec votre système`  

1. où êtes-vous quand vous ouvrez votre ligne de commande ?
2. quels sont les fichiers présents là aussi ?
1. déplacez-vous dans un répertoire où ça ne pose pas de problème de faire des tests
1. créez un répertoire test_ligne_commande
1.  allez dans ce répertoire


**Remarques** :

- on peut éditer des fichiers mais pas des répertoires !
- les fichiers et les répertoires comportent des méta-données (comme vos photos,emails,...) qui disent qui a le droit de faire quoi avec

**gestionnaires de fichiers** :

système|nom|pour ouvrir|racine
-------|--------|--------|------
windows|explorer|win+E| Lettre:\
mac|finder|cmd+N| /
linux|nautilus,gnome commander,...|commande|/

**super important** : pour éviter les problèmes (surtout en ligne de commande), toujours utiliser des noms de répertoires et de fichiers qui suivent ces règles :
- pas d'espace
- pas de caractères hors de :
  - l'alphabet anglais majuscule et minuscule
  - les chiffres arabes
  - le `_` (on tolère aussi le `-`)
- pas le nom d'un autre truc utile

**Remarque** : toutes les opérations que vous faites avec un gestionnaire sont faisable en ligne de commande (et souvent c'est plus pratique quand on a plein d'opérations à effectuer). Attention par contre, on a pas droit à l'erreur donc il vaut mieux avoir un système de suivi de version pour ses documents !



