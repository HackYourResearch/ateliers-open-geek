#Presentation de R et R Studio : 

Les formateurs : Thomas GARGOT et Pauline Perez

##Déroulement de la séance 

### Rappel de ce qu'est markdown : 

https://github.com/HackYourPhd/ateliers-open-geek/blob/master/Archives/Atelier%231.md

Bonnes pratiques : 

- commenter son code avec des # 
- utiliser des formats interopérables csv au lieu de xls ou bien du md plutôt que du doc 
- mettre sa base de données dans un fichier avec le script 
- une première étape difficile au final : trouver le chemin d'accès pour trouver son fichier csv ! 
- sur stackoverflow, vérifier la date de la réponse et méfiez vous des "vieux trucs" (car il peut avoir de nouveaux packages ou bien de nouvelle version) 

Dans Rmd, 

- on met le code R entre ``` et ``` ou aller directement dans l'onglet Code puis insert chunck
- on peut aussi écrire des phrases avec une fonction qui donnera directement le résultat sur le markdown 
Par exemple : il y a `r length(panama$company_name)` compagnies répertoriées dans cette base de données.


Base en R : 

- dim : nombre de colonnes et lignes
- str : type du fichier (ici dataframe) et type de chaque colonne (factor) 
- pour accéder à une colonne nom_du_fichier suivi d'un $ avec le nom de la colonne 
- head(nom de la colonne) : pour voir les dux premières lignes 
- lenght : longueur 
- unique : à utiliser dans le cas où on a plusieurs colonnes identiques, on en prend une seule.
- création de variable avec le nom_de la variable qu'on choisit <- 
- table() : tableau des effectifs du dataframe
- as.Date permet de transformer en data 

Base en R studio : 
- ne pas hésiter à aller voir l'aide ou bien exemplar 
- permet de voir les variables 

## Ressources : 

- Coursera https://fr.coursera.org/specializations/jhu-data-science
- Datacamp : https://www.datacamp.com/
- FUN : https://www.fun-mooc.fr/courses/UPSUD/42001S06/session06/about




