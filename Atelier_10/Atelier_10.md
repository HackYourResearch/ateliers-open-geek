# Atelier 10

* intro
* page statique
* exo xkcd
break
* demonstration crawler
* démonstration page dynamique
* exemples d'utilisation


## Introduction au webmining

### Qu'est ce que le webmining?

Le web mining (en français: extraction et fouille des données issues du web) est une **technique** d'extraction et de mise en valeur des données appliquées au web.

Le principe est simple:
* collecter des données en ligne (principalement des pages web)
* pour constituer des bases de données
* afin de les explorer par la suite.

### Principes de bases

#### Principes techniques

Le webmining est donc une technique qui repose sur les technologies du web et qui rentre dans la catégorie de l'extraction et analyse de données (Text and Data Mining).

Les principales opérations consistent à:
-   se connecter à une page web et charger le html (load, connect) dans le cas de page statique c'est une opération  simple, dans le cas de page dynamique c'est une autre paire de manches...
-   parcourir la page et extraire les informations cibles   (celles qui nous intéressent: ce qui implique d'avoir identifiés au préalalble les informations qui nous intéresse dans la page soit les balises )
- les stocker dans un fichier ou une base de données en les organisant selon ce qui nous arrange pour l'analyse
- analyser le résultat de cette extraction. Ici plein de techniques s'appliquent en fonction de l'analyse qu'on veut en faire.
  - La première des choses à faire est une **analyse statistique**: on a besoin de vérifier que les données sont complètes et consistantes. La phase classique de mise en cohérence des données
  - Une évitable phase de nettoyage est à prévoir: d'expérience, 90% du travail du "data miner" est de nettoyer les données, prévoir donc une longue phase qui s'ordonne selon la règle des 80% 20%.
  - Ensuite en fonction de l'hypothèse de départ, on mobilise des techniques différentes d'analyse text mining, extraction d'entités nommées, analyses de cooccurence, graphes de relations, classification, etc...

#### Cadre légal

Un petit rappel du cadre légal, le webmining est une technique d'extraction et de mise en valeur de données issues du web elle s'inscrit donc dans le cadre légal du TDM (Text and Data mining).

La pratique du text and data mining est complexe. Plusieurs choses à prendre en compte:
- législation sur le droit d'auteur et le copyright
- législation sur les données à caractère personnels
- droit des bases de données et données publiques
- législation sur les systèmes informatiques et Internet
A ces legislations s'ajoute une clause encore en débat sur l'exception de recherche, débattue lors de la loi pour une république numérique dont les amemdements acceptés sont en vigueur depuis Janvier 2017.

##### Droit d'auteur et copyright
- Le site en question est soumis au **droit d'auteur**, son accès libre sur Internet ne garantit pas que vous ayez le droit de reproduire tout et partie du site.
La réglementation en vigueur est donc soumise à celle du droit d'auteur et au code de la propriété intellectuelle.

D'un point de vue technique, votre adresse IP peut être bloquée par l'administrateur du site si vos appels sont trop insistants (banned) et que l'administrateur évalue que vos appels sont une menace pour la stabilité de son service (et oui on peut imaginer que cela s'apparente à une attaque par déni de service et que vous êtes un mechant pirate...)

D'un point de vue légal, une demande officielle doit être faite au site en question. En pratique (et c'est MAL), on utilise plein de techniques de pirate pour que nous verrons rapidement à la fin.

##### Réglementation du TDM

Selon la loi française, le TDM est soumis à une déclaration préalable à la CNIL qui implique de déclarer:

- la **nature des données** que vous collectez: données à caractère privé ou non. Si ces données sont à caractère privé un ensemble d'impératif de sécurité sont à mettre en place en conformité avec les recommandation de la CNIL (chiffrement, accès regulé aux données).

- le mode de collecte et de **stockage de ses données** :
tout comme pour une newsletter ou une inscription à un service, l'utilisateur concerné doit savoir quels usages vont être faire et on doit lui donner un moyen de se désincrire (l'optout est désormais interdit et l'optin par defaut: soit une case à cocher pour votre consentement éclairé)

 > S'informer sur toutes les recommandations de la [CNIL](https://www.cnil.fr/fr/comprendre-vos-obligations)

- **les traitements** qui vont être fait sur ces données:
croiser ces données avec d'autres implique de déclarer le mode de valorisation que vous aller en faire. Résolution d'adresse, extraction de relation

Il existe depuis janvier 2017 (loi pour une République Numérique), une exception à des fins de recherche, elle ne couvre que les travaux de recherche publique à vocation non-commerciale: il faut pour cela être affilié à un organisme de recherche publique et les conditions d'exercices sont encore flou.

C'est un point légal assez complexe que je vous invite à regarder avec la très bonne synthèse sur les enjeux et les questions que cela pose [scinfolex](https://scinfolex.com/2015/07/13/le-statut-juridique-des-donnees-de-la-recherche-entre-droit-des-bases-de-donnees-et-donnees-publiques/)


Par ailleurs, à terme et ce n'est pas encore legiféré par décret, ces données devront être transférées à un tiers de confiance (la BNF est présentie pour ce rôle dans le cadre des Archives du web français).

Pour etre tranquille, donc il vaut mieux exercer ces talents sur de données en **Open Data**.

Ici nous militons activement pour l'Open Science: à savoir l'accès à tous aux savoirs communs pour partage réutiliation et diffusion: cela passe aussi par une législation claire des modalités d'extraction et de manipulation des données du web pour faire science ensemble et de manière transparente.

Ensuite dans la pratique, beaucoup de professionnels ne s'embarassent pas de ces précautions légales qui peuvent être durement punies par la loi:
A titre indicatif: on peut condamner la personne jusqu'à 3 ans d'emprisonnement et de 45 000 euros d'amende.
Mais tout dépend de comment on considère le forfait:
- parasitisme économique
- vol de données
- intrusion dans un système informatique

Maintenant vous êtes prévenus !
