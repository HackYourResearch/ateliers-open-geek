#Atelier 4 : Cartographie d'acteurs


Cet atelier est l'occasion de revenir sur la cartographie et notamment la cartographie sociale. Son utilisation est facilitée aujourd'hui par l'utilisation de l'informatique, le web et les réseaux sociaux qui proposent des données struturées (ou non).

Pour une approche plus sociologique et historique, vous pouvez lire en complément cet [article](http://icolab.fr/2014/12/cartographier-construire-ponts).

##Agréger des données sur des réseaux sociaux 

###Facebook

Commençons par Facebook et l'application [Netvizz](https://tools.digitalmethods.net/netvizz/facebook/netvizz/) qui va permettre d'exporter son réseau Facebook, que l'on peut augmenter avec les pages qu'aiment nos amis.
Il est aussi possible d'exporter des données concernant des groupes ou des pages Facebook. 

*/!\ Facebook anonymise les données dans le cas des pages et des groupes.*

Netvizz génère un fichier [GDF](http://guess.wikispot.org/The_GUESS_.gdf_format) que vous pourrez ouvrir avec Gephi par exemple.


###Twitter, Youtube, Flick, MediaWiki, VK

Pour travailler sur ces réseaux, un outil simple et très complet est [NodeXl](https://nodexl.codeplex.com/).

*/!\ NodeXl est un template Excel et ne fonctionne que sur Windows. D'autres outils comme [Bluenod](http://bluenod.com/) existent même s'ils traitent souvent un seul réseau. Pour ceux plus avancés avec Python, [NetworkX](http://networkx.github.io/) permet de travailler avec de nombreux réseaux et de travailler vos graphes. Un prochain atelier traitera de NetworkX*

NodeXl rajoute un onglet dans le classeur Excel qui offre la possibilité d'importer ou d'exporter des données.
En sélectionnant import, il est possible de voir les réseaux sociaux supportés et le nom donne une idée des données que nous pouvons obtenir.
Une fois que nous les avons choisies, une interface permettant de configurer NodeXl apparaît et nous pouvons spécifier les comptes qui nous intéressent par exemple et la profondeur des relations entre les comptes.

Une fois les données récupérées, il est possible de les exporter dans des formats graphes : [Pajek](http://pajek.imfm.si/doku.php?id=pajek) et/ou [GraphML](http://graphml.graphdrawing.org/) pour les traiter avec Gephi.

Voici un [tuto vidéo](http://www.connectedaction.net/2009/11/11/video-using-nodexl-to-map-the-digg-mentioning-twitter-population/) (un peu vieux mais qui vous donnera une idée du fonctionnement de NodeXl). Sur ce [OneDrive](https://onedrive.live.com/?cid=ae935b3cde8015dd&id=AE935B3CDE8015DD!465) vous trouverez d'autres ressources complémentaires. 
Et la meilleure solution pour apprendre est de tester :-)

###Relations entre des sites web

Allons plus loin, si vous souhaitez observer les relations hypertexte entre des sites internet, [IssueCrawler](https://www.issuecrawler.net/index.php) vous permettra de réaliser cela très simplement.
L'outil, développé aux Pays-Bas, est très complet et performant. Il suffit de rentrer une liste d'URL et de configurer le nombre de pages que vous souhaitez qu'il crawl, la profondeur du crawl ... et votre crawl est mis dans la liste d'attente. Il faudra attendre un petit moment avant que le crawl soit fini (vous le verrez dans la liste d'attente à droite). Vous pourrez après récupérer le résultat dans de nombreux formats (XML, txt ou [GEXF](http://gexf.net/format/) notamment). Après vous pourrez retraiter les données obtenues encore sur Gephi.

###Mettre en forme les données obtenues

Pour la mise en forme des données obtenues, nous utilisons [Gephi](http://gephi.org/) qui est un logiciel libre multi-plateforme.

Après l'import des données dans le logiciel, vous pouvez les mettre en forme. Pour bien commencer, sur le site de Gephi, vous trouverez de nombreuses ressources en fonction de vos besoins (en effet, il est possible de réaliser beaucoup de choses avec Gephi ! Il semble compliqué et présomptueux de vouloir tout couvrir ici).

Deux ressources pour Gephi qui pourront déjà répondre à nombre de vos questions : 
- [Tutos sur Gephi.org](https://gephi.github.io/users/)
- [Site de Clément Levallois](http://www.clementlevallois.net/gephi.html)

Et n'hésitez pas si vous avez des questions :-)
