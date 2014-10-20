# [Présentation générale](https://github.com/karthik/webnativesci)

# Le language Markdown
[Markdown](http://daringfireball.net) est un moyen de faire à la fois du code et du commentaire de code. Une excellente alternative à Microsoft Word pour la prise de note et même l'écriture de documents plus importants (e.g. écriture d'article avec citation de références bibliographiques : [Scholarly Markdown](http://blog.martinfenner.org/2013/06/17/what-is-scholarly-markdown/)).

## Logiciels d'édition Markdown
Sur Mac, l'application [Mou](http://25.io/mou/) est fortement recommandée car elle autorise l'édition Markdown tout en ayant un aperçu du résultat final en temps réel.

Sinon, il existe des éditeurs Markdown en ligne (prendre bien garde à sauvegarder, en local, le document rédigé):
- http://markable.in/editor/
- http://dillinger.io/

Sur Mac/PC/Linux, l'éditeur [Sublime Text](http://www.sublimetext.com) permet d'éditer du Markdown (mais aussi du Python). Pour avoir un aperçu en temps réel du résultat Markdown, il suffit de suivre quelques étapes :
0. Installer "Package control" en suivant les instructions [ici](https://sublime.wbond.net/installation).
1. Installer le package "Markdown Preview" : faire 'Ctrl-Shift-P + "Install Package", et dans la liste qui apparait, taper "Markdown Preview" pour trouver et installer le package.
2. On "compile" le fichier Markdown en HTML en faisant "Ctrl-B" dans Sublime Text et on ouvre le fichier créé dans son navigateur internet. Grace au plugins [AutoReload sur Firefox](https://addons.mozilla.org/fr/firefox/addon/auto-reload/) ou [Tincr sur Chrome](http://tin.cr), à chaque "Ctrl-B", le navigateur va recharger le fichier HTML et afficher le beau markdown qu'on a écrit.

Sur Windows ? Il y a en tout cas un émulateur de terminal Linux pour Windows: [Cygwin](https://www.cygwin.com).
Pour programmer confortablement en Python sous Windows: http://sametmax.com/programmer-confortablement-en-python-sous-windows/

## Les bases de Markdown

Notes :
- L'extension de fichier Markdown est le ".md"
- Il faut savoir faire les [] ainsi que le ~ sur son clavier.

Notions abordées: les styles (gras, italique, souligné, barré), les titres, les listes, les liens, et les images.

Mettre une image qui vient de son propre ordinateur : il faut indiquer soit le chemin relatif, soit l'absolu de l'image considérée. Il est conseillé de mettre dans le même répertoire le fichier ".md" et les images qui y sont insérées. Pour plus de clarté, on peut également créer un répertoire "images" dans le répertoire du fichier ".md"

Pour un résumé en français des commandes de base, il y a un [excellent tutoriel sur OpenClassRooms](http://fr.openclassrooms.com/informatique/cours/redigez-en-markdown).

# Bases de la programmation

# Installer Python
Nous allons utiliser l'installation Anaconda de Python: http://continuum.io/downloads
L'intérêt d'Anaconda est d'installer python de manière directe et que beaucoup de packages utiles sont déjà fournis.

# Base de la ligne de commande
Installation d'un autre terminal (pour Mac: [Iterm2](http://iterm2.com/), pour Windows: [cmd](http://windows.microsoft.com/en-us/windows-vista/open-a-command-prompt-window), pour Linux: [20 Useful Terminal Emulator](http://www.tecmint.com/linux-terminal-emulators/)).

Premières notions abordées : ls / cd / cd .. / la tabulation pour compléter un nom.

Guides en français assez complets pour [Windows](http://fr.openclassrooms.com/informatique/cours/apprenez-a-developper-en-c/la-ligne-de-commande-3) et [Linux/Mac](http://lea-linux.org/documentations/Fiches:La_ligne_de_commande).

# Questions

# Idées pour les prochains ateliers

## Thêmes:
- Coding III
- Programming (I) II
- Debuguer du code

- Image processing
- Collecter, traiter analyser des données data analysis I
- Visualisation de données
- Analyse de données en imagerie et de données issues d'expérience comportementales
- Statistiques

- Écrire des articles (pandoc)
- Veille autour des initiatives non gouvernementales et non privés autour de la programmation et de la donnée
- Cartographie 
- Connaitre l'infrastructure des réseaux / Social Network Analysis 
- Social media II

## Languages/Outils:
- R I
- Python II
- Github I
- Twitter I
- Haddoop html/CSS
- Ruby

## Autre:
- Santé mentale? o.O
