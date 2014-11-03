# Retour sur les Bases
## Votre Ordinateur

### Le matériel
le **processeur** manipule des 0 et des 1 écrits en mémoire en suivant une instruction.

La **mémoire** de votre ordinateur :

 - la mémoire vive (l'information s'efface quand on coupe le courant)
 - le disque dur (l'information reste tant que pas modifiée)

Les **langages** informatiques permettent d'écrire des instructions de façon un peu moins pénible qu'avec des suites de 0 et de 1 :

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



