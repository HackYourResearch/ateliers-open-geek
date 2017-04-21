## Installer des bibliothèques externes

Python vient avec un système pour installer des modules complémentaites et spécifiques qu'on appelle `pip`
`Pip` permet de télécharger automatiquement les bibliothèques dont on a besoin


### Vérifiez que pip est bien installé sur votre machine
dans le terminal, tapez
```
$ pip --version

```
Cette commande affiche la version de pip
```
pip 9.0.1 from /usr/local/lib/python3.5/dist-packages (python 3.5)
```
#### Installer pip
Si , par malheur, le terminal vous affiche:
```
La commande « pip » est introuvable
```
Il faut l'installer, pour cela **téléchargez** pip

* par exemple en ligne de commande:
```
wget https://bootstrap.pypa.io/get-pip.py
```

* ou simplement en ouvrant le navigateur, télécharez et enregistrez le fichier dans un dossier accessible

Puis executez en ligne de commande:

```
python get-pip.py
```

### Téléchargez les bibliothèques requises

Pour cet atelier nous avons besoin de :
numpy
networkx
matplotlib

```
pip install numpy networkx matplotlib
```

si ca ne marche pas ajoutez sudo au début de la commande précédente et relancez
Le terminal devrait vous afficher le message suivant

```
Successfully installed <nom_de_la_libraire.version>
```

### Importer les librairies dans votre script

Utiliser des librairies externes demande de déclarer à Python que nous allons les utiliser pour cela
on utilise l'instruction `import`
Un fichier de script python appelons-le `exemple.py`
commence toujours par:

- la **déclaration du langage utilisé** (sheebang)
une bonne pratique pour spécifier quel version et dans quel dossier se trouve installé python
```
!usr/bin/python3.5
#si vous travaillez dans un environement précisez-le
!usr/bin/env python
```
Il est ensuite immédiatement suivi d'un espace puis d'une déclaration des bibliothèques externes que nous allons utiliser aec la commande `import`

```
import numpy
import matplotlib
import networkx
```
