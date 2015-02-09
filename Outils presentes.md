#Liste et présentation des outils des ateliers OpenGeek

## Outils pour le MarkDown : les éditeurs

### Pour Mac

- [Mou](http://25.io/mou/). Téléchargeable est installable. Il permet de visualiser en direct ce qui est rédigé en MarkDown. L'outil propose de nombreuses options comme la création de vos thèmes, de changer le CSS ...

- [Sublime Text](http://www.sublimetext.com). Cet éditeur de texte vous permettra aussi d'éditeur du MarkDown ou d'autres langages.

Pour avoir un aperçu en temps réel du résultat Markdown, il suffit de suivre quelques étapes :

1. Installer "Package control" en suivant les instructions [ici](https://sublime.wbond.net/installation).

1. Installer le package "Markdown Preview" : faire 'Ctrl-Shift-P + "Install Package", et dans la liste qui apparait, taper "Markdown Preview" pour trouver et installer le package.

1. On "compile" le fichier Markdown en HTML en faisant "Ctrl-B" dans Sublime Text et on ouvre le fichier créé dans son navigateur internet.

### Pour Windows

-  L'éditeur [Sublime Text](http://www.sublimetext.com)est aussi disponible pour Windows. La procédure pour visualiser en direct le MarkDown est la même.

### Pour Linux

- L'éditeur [Sublime Text](http://www.sublimetext.com) est aussi disponible pour Linux. La procédure pour visualiser en direct le MarkDown est la même.

#### En ligne

Sont disponibles en ligne les éditeurs suivant (prendre bien garde à sauvegarder, en local, le document rédigé) :
- L'éditeur [Markable](http://markable.in/editor/). L'export peut se faire directement en HTML ou en MarkDown.
- L'éditeur [Dillinger](http://dillinger.io/). Vous pouvez visualiser en direct le rendu HTML. L'éditeur offre la possibilité d'exporter en HTML, MarkDown, PDF ou/et de l'enregistrer dans des espaces en ligne comme GitHub, Dropbox, Google Drive ou One Drive.


## Outils pour le Python

### Pour Windows, Mac, Linux

- [Anaconda](http://continuum.io/downloads) est un outil simple qui permet d'installer facilement Python et de nombreux packages


#Liste des commandes présentées lors des ateliers OpenGeek

La ligne de commande est un moyen de communiquer directement avec son ordinateur. Tous les OS proposent un accès à la ligne de commande.

## Avoir la ligne de commande 

### Windows

- Un terminal est disponible, pour y accéder, cherchez le programme cmd.exe ou faites win+R puis cmd.
- Il est existe un émulateur de terminal Linux : [Cygwin](https://www.cygwin.com). Cygwin vous donnera accès à de nombreux outils libres disponibles sur Linux pour bénéficier des fonctionnalités du terminal.
Exemple : exécuter un script .sh

### Pour Mac 

- Un terminal est disponible par défaut et simplement (pour Mac si vous ne le trouvez pas, faites une recherche depuis le Spotlight).
- Pour Mac, d'autres terminaux sont disponibles comme [Iterm2](http://iterm2.com/)

### Pour Linux 

- Si vous utilisez Linux, vous devez savoir un minimum utiliser la ligne de commande (au moins comment obtenir un terminal).
- Il existe de nombreux terminaux que vous pouvez utiliser sur Linux suivant vos besoins.

## Utiliser la ligne de commande 

### Les commandes de base 

1) Se situer

- `pwd` : renvoi le dossier dans lequel nous sommes (Mac et Linux)
- `chdir` : renvoi le dossier dans lequel nous sommes (Windows)

2) Se déplacer dans les dossier 

(pareil pour les différents OS. /!\ sur Windows, il faut utiliser \ et non pas le / pour le chemin des dossiers). 

- `cd` : permet de changer de dossier

Exemple : `cd /chemin_vers_le_dossier_qui_nous_interesse`
- `.` : signifie que c'est le dossier dans lequel nous sommes actuellement.

Exemple : je suis dans le dossier /root/usr/. Je veux aller dans le dossier /root/usr/local/.Cela donne la commande : `cd ./local`
- `..` : représente le dossier dans lequel est situé notre dossier.

Exemple : je suis dans le dossier /root/usr/local. Je veux retourner dans /root/usr/. Cela donne : `cd ..`

3) Connaitre le contenu d'un dossier
- `ls` : permet de lister les fichiers dans le répertoire
- `ls -al` : permet de lister les fichiers avec des informations comme la taille, le propriétaire du fichier ou la date de création.
