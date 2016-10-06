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

### Internet

#### Réseaux domestiques, FAI

##### **&#65311;** De quoi a-t-on besoin pour se connecter à l'Internet?

Internet, est une technologie qui nécessite plusieurs éléments pour arriver jusqu'à nous. Dans les choses auquelles nous avons directement accès, on trouve :

- Un périphérique (ordinateur, téléphone, console de jeu, frigo connecté ...) qui va être notre porte d'entrée, physique (hardware) vers ce vaste monde
- Un logiciel (un client - on y reviendra) qui nous offre un service autour d'internet (le navigateur qui donne accès aux pages web, skype qui nous donne accès aux conversations instantanées, ...)
- Une liaison à un réseau de télécommunication approprié : internet arrive à la maison ou au bureau via une prise qui est reliée au réseau téléphonique, au réseau cablé, au réseau fibré voir au réseau satellite
- Un accès internet, via un fournisseur d'accès internet (FAI), qui est une entité qui gère ce réseau de télécommunication et vous en autorise l'accès tout en assurant sa gestion technique, son entretien
- Un modem et un routeur, souvent contenus dans la box du FAI, qui assurent la liaison entre chez nous et le réseau de télécommunication ; ils servent à la fois de douanier, de tour-operator, de police des frontières, d'ambassade ... ;)

##### &#x1f441; De mon ordinateur à la page web

Mais sur le réseau au delà de nos murs s'étendent de nombreux autres éléments nécessaire au fonctionnement et à l'utilisation d'Internet.

Un bon moyen d'explorer ce vaste monde est de décomposer ce qu'il se passe lorsqu'on accède à une page web dans un navigateur. Cette aventure est UN exemple d'utilisation d'Internet, plus précisément une exploration du "World Wide Web" (ou plus simplement le Web), une sous-partie d'Internet.

Ordinateur allumé, branché à Internet, navigateur lançé (logiciel client - Chrome, Firefox, Internet Explorer, ...), nous allons "naviguer" vers un site du "World Wide Web", par exemple `http://perdu.com/` en tappant celà dans la barre d'adresse du navigateur.

Celà, c'est une adresse web. Un ensemble d'informations qui désignent à la fois une "ressource" disponible sur internet, et comment y accéder.

`perdu.com` désigne la ressource, sous une forme facile à mémoriser et utiliser pour un humain : le nom de domaine. `http` désigne le 'protocole' que l'on va utiliser pour accéder à cette ressource. Le protocole c'est les conventions qui font qu'on arrive à communiquer : quel language on va communiquer, est-ce qu'on se sert la main avant de se présenter, est-ce qu'on enlève son chapeau pour respecter son hôte, ... ?

Quand on va naviguer, le client va envoyer un message suivant le protocole fourni, à une entité sur internet qui va analyser le nom de domaine pour indiquer au navigateur à qui parler pour avoir la page web. Cette entité c'est le "serveur DNS" (DNS : Domain Name Service).

Pour identifier "à qui on parle", sur Internet, on utilise une adresse un peu moins lisible que le nom de domaine, c'est l'adresse IP, un ensemble de nombre sous la forme suivante : `208.97.177.124`.

Let's play : le site http://ping.eu/nslookup/ permet d'obtenir l'adresse IP liée à un nom de domaine.

Nom de domaine   | Adresse IP
---------------- | ----------------
perdu.com        | 208.97.177.124
google.com       | 172.217.22.174
fr.wikipedia.org | 91.198.174.192

Armé du protocole et de l'IP de notre serveur de destination, le navigateur va pouvoir aller interroger ce serveur pour récupérer la ressource et l'afficher. Dans notre cas, afficher une page web.

#### Serveurs et protocoles

##### **&#65311;** Protocole de communication



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
