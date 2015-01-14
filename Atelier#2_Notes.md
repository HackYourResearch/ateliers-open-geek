#Notes collaboratives de l'atelier OpenGeek#2

Storify de [l'atelier #openGeek2](https://storify.com/HackYourPhd/opengeek-2-ordinateur-ligne-de-commande-et-premie#publicize)


##Quelques bases sur l'ordinateur

**L'interface de l'ordinateur**

La 1ère interaction utilisateur-ordinateur a lieu a travers l'interface graphique, spécifique au système d'exploitation.
L'interface graphique est limitée par ce que le concepteur autorise a l'utilisateur

Différence entre répertoire et un fichier : 
    - le repertoire contient des fichiers.
    - le fichier contient des données sous différents formats.
    
**Qu'est-ce-qu'un ordinateur ?**

->Disque Dur+ Mémoire vive + Processeur<-

+ Disque dur  
    + disque et roulement à bille : tête de lecture microsillon 
    + information codée sous forme de 0 et 1 information réinscriptible ==> conservation même quand l'ordi est éteint
        
+ Mémoire Vive : RAM
+ Processeur : transforme info du disque dur selon les commandes qu'on lui donnent


**Comment interagir avec l'ordinateur (sans parler en 0 et 1) ?**

A la base, carte perforée (année 1950),
maintenant langages utilisant la ligne de commande

ligne de commande: 
        mode de conversation direct avec l'ordinateur

Ordinateur : interprète les choses qu'on lui demande, 
on doit apprendre à communiquer avec lui avec un langage particulier 
pas de sous-entendu chez l'ordinateur. 

##Lignes de commande

**Ouvrir une fenêtre de commande**

pour ouvrir une fenêtre de commande  
- sous Mac : répertoire application> Utilitaires/Utilities>Terminal
- sous Windows : win+R puis cmd on peut aussi utiliser powershell (installation quand on met git) 
    Afficher un bureau window depuis un navigateur
    On peut choisir son système d'exploitation sur la partie droite.
    
*Pour connaître l'interface Windows quand on est sur Mac*  [http://screenshots.modemhelp.net/](http://screenshots.modemhelp.net/)
 
 **Arborescence de fichier** 
 
Trouver la racine : 
Conseil dans votre finder (indiquez votre disque dur : la racine) et afficher la barre de chemin d'accès

**Système de fichier** 
    alphabet avec lequel on écrit les données sur le disque dur  
    problème pas compatible parfois entre Windows, Linux et Mac  
    le Fat32 est compris par tous mais limite à 4Go  
    le NTFS passe entre Linux et Windows pas Mac
    
**Lignes de commande : la base**
    
sigle $ sur Mac ou > sur Windows <== signifie que c'est vous qui  avez la main (dialogue avec l'ordinateur : jamais deux personnes qui  parlent en même temps) 

+ se reperer dans l'arborescence :
**pwd** sur mac **chdir** sur Windows 
+ changer de repertoire : 
**cd** sur unix(mac)/windows
+ afficher tous les sous-repertoires (liste des elements dans le repertoire): **ls** sous unix(mac) **dir** sous windows
**ls -l** liste les fichiers mais avec bcp plus de détails

Pour naviguer flèche du haut flèche du bas pour savoir ce que l'on a taper avant ou après 

##Quelques explications sur Github

**Github**
 
 + réseau social pour partager du code 
 + document mis en public sauf si on paye
 + facilite la collaboration

**Récupération de fichier sur Github**

*Downloadzip* pour télécharger les fichiers
on peut ouvrir les fichiers .md sur un éditeur de classique ou bien avec une appli spécialisée markdown 


##Premier pas sur Python

**Langage python** 
langage relativement récent crée en 1991 : facilement accessible et très modulaire

"python" pour démarrer python puis ensuite on est en langage python
**help()** comande la plus simple pour sortir de help taper **quit**
on peut aussi nommer un modules particulier help('....')

**help>** signifie que l'on est dans le système d'aide de python


**modules/librairies**

ensemble de la boite à outils pour obtenir des fonctionnalités 

+ **import** permet d'avoir accès à un module (tant qu'on n'a pas fait import on n'y a pas accès) 
**os** nous permet d'utiliser les fonctionnalités de os (ligne de commande).os est une librairie 

+ **fonction help :**
help(os.getcwd) aide sur la fonction os.getcwd 
help(os) aide sur le module os
q pour quitter l'aide

+ *get cwd()*
os.getcwd() quel est le repertoire courant?

+ *os.listdir(path)* fonction qui a besoin de l'argument ici path
path = liste structurée , donne le chemin du repertoire
*os.listdir(path)* liste tous les éléments du repertoire specifié

+ *os.chdir("repertoire")* pour changer de repertoire courant
os.listdir(os.getcwd())

**type d'erreur**
erreur de Syntaxe "SyntaxError" "TypeError"
"AttributeError" "NameError"

**Nota Bene :** 

+ le ; sépare deux instructions en python et autre langage 
+ bien mettre les ()
+ les "..." indiquent que l'on écrit du texte
+ Eviter les accents, les caractères bizarres, les espace,les chiffres arabes, les_ 
+ souvent on a des espaces qui se rajoutent
+ Utiliser Stackoverflow et Google 
+ Bien documenter son code

Attention :
    Python fait du calcul sur des entiers
    sinon on utilise float astuce on peut mettre le chiffre suivi d'un .

quitter python quit()

## Apprendre Python et Ipython Notebook

Environnement de travail dans lequel on code: IPython
Pour ouvrir dans la fenêtre de commande: "ipython notebook"


**Sites pour apprendre python :** 

[OpenClassrooms](http://openclassrooms.com/courses/apprenez-a-programmer-en-python)
[Cours Master](http://www.dsimb.inserm.fr/~fuchs/python/)



**Ipython Notebook** 

[http://ipython.org/notebook.html](http://ipython.org/notebook.html) 
pour quitter ipython notebook : `ctrl c` dans la fenetre du terminal où on l'a lancé.

le cahier peut aider à communiquer avec les autres utilisateurs (possibilité d'écrire en markdown)
on peut exporter ensuite le notebook ipython en différent format .py .html 


##Résumé du dernier atelier 

Liens utiles :
 
- [Github HackYourPhD](https://github.com/HackYourPhd/ateliers-open-geek) pour les résumés en markdown]
- Le [groupe](https://groups.google.com/forum/?hl=fr#!forum/open-geek) pour les infos pratiques : demander à rejoindre le groupe si vous voulez les infos pratiques et les futures dates.
- Le lien vers le [storify](https://storify.com/Colab/atelier-opengeek-code-week-ue) du premier atelier.
