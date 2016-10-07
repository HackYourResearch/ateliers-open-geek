***[Culture GG] Atelier 02***
# Internet, web et réseaux

Nous utilisons Internet tous les jours, mais qui sait vraiment comment ça marche ? Ouvrons la boîte de pandore et explorons les bases de notre environnement numérique quotidien:
* Que se passe-t-il quand on se connecte à **Internet** ?
* Comment marche un **site web** ?
* Qu’est-ce qu’il y a derrière **Firefox** ou **Skype** ?
* Comment marche un **moteur de recherche** ?
* Qu’est-ce qu’une **app** ?
* Que savent de mes voyages sur la toile mon **fournisseur d’accès**, **Google** ou la **NSA** ?
* Comment conserver un semblant de **vie privée** ?

De quoi naviguer en sachant vraiment où on met les pieds, en toute tranquillité et en toute conscience !


## Sommaire

### [Internet](#internet-1)

#### [Réseaux domestiques, FAI](#réseaux-domestiques-fai-1)
* **&#65311;**De quoi a-t-on besoin pour se connecter à l'Internet?
* &#x1f441; De mon ordinateur à la page web

#### [Serveurs et protocoles](#serveurs-et-protocoles-1)
* **&#65311;** Protocole de communication
* **&#65311;** HTTP

#### [World Wide Web](#world-wide-web-1)
* **&#65311;** Internet = InterconnectedNetwork
* &#x1f441; Le World Wide Web
* &#x261e; HTTP et le web

#### [Le site web](#le-site-web-1)
* &#x1f441; Le site web
* &#x1f441; Client/Serveur
* &#x1f441; Les éléments d'un site web
* &#x261e; Ma première page HTML

### [Moteur de recherche](#moteur-de-recherche-1)
* &#128249; Comment marche un moteur de recherche?
* &#x1f577; Collecter, Indexer, classer: le robot-araignée
* &#x1f577; Les algorithmes de recherche et de ciblage
* &#127850; Données personnelles, cookies

### [Les "évolutions" du web](#les-évolutions-du-web-1)
* Web 1.0: documents
* Web 2.0: personnes
* Web 3.0 **&#x1f577;**: sémantique (sens)
* Web&#xb2;: physique (objets)

### [Censure et vie privée](#censure-et-vie-privée-1)
* &#x1f512; Techniques de censure


## Contenu

### &#x1f441; De mon ordinateur à la page web

#### **&#65311;** C'est comme au restaurant !

Quand on navigue sur le web, on évolue généralement dans ce qu'on appelle un `environnement client-serveur`. En gros, un restaurant. Ce concept présente d'un côté le `client`, celui qui va demander quelque chose (une crème au chocolat, un cocktail ou une page web) et le `serveur`, qui va faire ce qu'il faut pour lui apporter.

Naviguer sur internet, cela revient donc à un échange entre le `client` et le `serveur`, ponctués de discussions et d'actions.

Le `client` est à l'origine de la demande, pointe son nez dans le restaurant, demande au placeur où s'asseoir puis fait une `requête` au serveur, en suivant certains protocoles. Pas question de mal parler au serveur, auquel cas il risque de crasher dans notre plat.

Le serveur va prendre notre commande si elle est à la carte, puis vas s'enquérir d'aller chercher notre plat, éventuellement en demandant à différents collègues de lui assembler les ingrédients nécessaires.

#### **&#65311;** De quoi a-t-on besoin pour se connecter à l'Internet?

Internet, est une technologie qui nécessite plusieurs éléments pour arriver jusqu'à nous. Une partie de ces éléments sont directement à notre contact et constituent donc le minimum à posséder pour explorer ce vaste monde. Techniquement, on troque donc la tenue correcte, la carte bleue et l'estomac affamé contre les choses  suivantes :

- Un périphérique (ordinateur, téléphone, console de jeu, frigo connecté ...) qui va être notre porte d'entrée, physique (hardware) vers ce vaste monde
- Un logiciel (un client - on y reviendra) qui nous offre un service autour d'internet (le navigateur qui donne accès aux pages web, skype qui nous donne accès aux conversations instantanées, ...)
- Une liaison à un réseau de télécommunication approprié : internet arrive à la maison ou au bureau via une prise qui est reliée au réseau téléphonique, au réseau cablé, au réseau fibré voir au réseau satellite
- Un accès internet, via un fournisseur d'accès internet (FAI), qui est une entité qui gère ce réseau de télécommunication et vous en autorise l'accès tout en assurant sa gestion technique, son entretien
- Un modem et un routeur, souvent contenus dans la box du FAI, qui assurent la liaison entre chez nous et le réseau de télécommunication ; ils servent à la fois de douanier, de tour-operator, de police des frontières, d'ambassade ... ;)

#### **&#x1f441;** Le navigateur et sa barre d'adresse

Ça y est, on est faim prêt, on peut entrer dans le restaurant. Pour se faciliter la vie, on a regardé la carte, avant de venir et on sait ce qu'on veut : une bonne part de `http://perdu.com`, l'adresse web qui nous fait envie. On lance donc notre navigateur web et on annonce ce qu'on veut en rentrant cette adresse dans la barre ... d'adresse.

Cette adresse, elle contient deux informations :
- `perdu.com` désigne ce qu'on est venu chercher. Cela représente une ressource, disponible quelque part sur internet, un plat que le restaurant présente à la carte ;
- `http` est le protocole, c'est à dire les conventions qu'on va utiliser pour discuter avec les employés du restaurant, pour que tout se passe bien : j'enlève mon chapeau en rentrant, j'ai mit une belle cravate pour venir au McDo, je parle poliment, j'ai de quoi payer dans mes poches, je parle la même mangue que le serveur ...


#### **&#65311;** Protocoles de communication

De protocoles, dans les "télécommunications", il y en a partout ! Et l'informatique, ça fricotte pas mal avec les télécommunications. Donc on en trouve partout !
Certains sont des protocoles pour faire communiquer les appareils, et donc sont des éléments préalables au fonctionnement d'Internet, par exemple :
- le `WiFi`, protocole qui va expliquer à votre téléphone comment se relier à votre box ;
- l'`Ethernet` et, par exemple, son ami le `PPPoE`, qui vont expliquer à votre ordinateur comment discuter avec votre fournisseur d'accès via la box.
D'autres protocoles sont des protocoles liés à toutes les belles choses qu'on peut faire avec Internet :
- le SMTP, qui va expliquer à votre logiciel de messagerie comment envoyer un e-mail à votre tante ;
- le BitTorrent, qui va expliquer à votre logiciel de téléchargement comment échanger avec autrui tout ces supers films de vacances ;
- le HTTP, qui va expliquer à votre navigateur comment on va récupérer une page web pour passer une nuit entière à surfer sur wikipedia.

##### Le HTTP : HyperText Transfer Protocol

Regardons ce HTTP de plus prêt : ce protocole définit un certain nombre d'actions et explique comment faire une phrase pour décrire quelle action on veut faire.
Ces actions, ce sont par exemple :
- GET : pour aller récupérer une ressource, une page web par exemple (c'est l'action par défaut que fait le navigateur)
- POST : pour envoyer des données histoire de faire évoluer une ressource
- DELETE : pour supprimer une ressource
- ...

Finalement, quand on tape `http://perdu.com`, notre client, le navigateur, envoie une `requête` `GET` sur Internet pour récupérer la ressource `perdu.com`.

##### &#x1f441; L'adresse web, qu'est ce qu'on en fait ?

Au restaurant, passer commande est assez facile : le serveur se pointe à la table et fait des ronds de jambe, puis écoute vos désirs.

Internet, c'est un peu plus comme un McDo : vous vous pointez avec la faim au ventre, c'est un peu le bordel, vous savez pas où aller, vous vous dirigez finalement vers une borne à qui vous faites la commande et qui vous redirige vers le bon comptoir : après un peu de latence vous aurez enfin votre porn food.

Quand le navigateur envoi sa requête (en HTTP avec l'action GET vers perdu.com), il l'envoi à un premier acteur d'internet : le serveur `DNS`. Toujours le même : celui que nous fourni notre fournisseur d'accès automatiquement, ou un qu'on a configuré dans son ordinateur ou sa box.

DNS, ça veut dire "Domain Name Service" (service de nom de domaine) et ça se charge de comprendre ce que vous avez commandé. Et oui, en vrai, pour savoir où sont les ressources, sur Internet, on utilise des adresses pas vraiment sexy à manipuler : les adresses IP. Ça ressemble à ça : `208.97.177.124`.

L'humain que nous sommes étant beaucoup plus à l'aise avec des lettres formant des mots intelligibles, on a créé le concept de "nom de domaine", le fameux `perdu.com`. On a donc le serveur `DNS` qui se charge de traduire `perdu.com` en `208.97.177.124`.

###### Let's play

Le site http://ping.eu/nslookup/ permet d'obtenir l'adresse IP liée à un nom de domaine.

Nom de domaine   | Adresse IP
---------------- | ----------------
perdu.com        | 208.97.177.124
google.com       | 172.217.22.174
fr.wikipedia.org | 91.198.174.192

##### En cuisine

Une fois équipé de cette adresse IP, votre navigateur peut continuer son périple : envoyer sa requête au serveur `208.97.177.124`.

Le serveur va recevoir cette requête, comprendre ce qu'on lui demande, filer la commande à son cuistot. Le cuistot va identifier les ingrédients, filer des instructions à ses commis, mettre tout ça dans une assiette, avec un peu de cuisson soupoudré sur le tout et le serveur, le plat en main, va le rapporter au client.

La tambouille en cuisine, c'est ce qu'on appelle le "développement backend". Les trucs qu'on voit pas. On peut faire ça en Python, en PHP, en Java, bref, en un peu prêt n'importe quel langage de programmation. On peut même en utiliser plusieurs à la fois : le cuisto et les commis ont leur propres techniques, leur propre savoir faire.
En plus du petit personnel, on va trouver plein d'autres choses indispensables : bases de données (les réfrigérateurs), autres serveurs qui vont fournir des ressources essentielles à la composition de la ressource demandée (un peu comme un restaurant, qui est lui même client de ses fournisseurs d'ingrédients bruts).

Dans les assiettes qui sortent des cuisines, on trouve de tout : entrées, plats, desserts, cocktails, cachouètes ... C'est à dire qu'une requête auprès d'un serveur peut demander la récupératio d'une page web, mais aussi, plus simplement, d'une image, d'une musique, d'une vidéo ...

Si tout le monde sait à peu près ce que sont ces derniers types de fichiers, la page web est quelque chose de plus mystérieux, composé en grande partie d'un ingrédient magique : le HTML.

##### Le HTML, l'ingrédient préféré du World Wide Web

Le HTML



##### **&#65311;** HTTP

#### World Wide Web
##### **&#65311;** Internet = InterconnectedNetwork
##### &#x1f441; Le World Wide Web
##### &#x261e; HTTP et le web

#### Le site web
##### &#x1f441; Le site web
##### &#x1f441; Client/Serveur
##### &#x1f441; Les éléments d'un site web
##### &#x261e; Ma première page HTML

### Moteur de recherche
##### &#128249; Comment marche un moteur de recherche?
##### &#x1f577; Collecter, Indexer, classer: le robot-araignée
##### &#x1f577; Les algorithmes de recherche et de ciblage
##### &#127850; Données personnelles, cookies

### Les "évolutions" du web
##### Web 1.0: documents
##### Web 2.0: personnes
##### Web 3.0 **&#x1f577;**: sémantique (sens)
##### Web&#xb2;: physique (objets)

### Censure et vie privée
##### &#x1f512; Techniques de censure
