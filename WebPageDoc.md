# Documentation technique "Lavos - plateforme de laverie en ligne de l'INSA Lyon"

Ce site est construit avec Vue pour l'interface utilisateur (frontend) et Django pour la gestion de base de données et la communication avec l'api des machines à laver de l'INSA (backend). Axios, un module javaScript, est utilisé du coté Vue pour faire des requêtes sur le backend Django.

Le backend en Django questionne actuellement une api factice codée en python avec Flask simulant les données des machines à laver. Effectivement, le travail de récupérer les données des machines à laver, de les traiter et de les présenter via une api sort du cadre de ce projet et sera réaliser par le Clubelek en partenariat avec le BDE de l'INSA de Lyon.

## Vue
Les modules de Vue utilisé sont "Vuetify" et "router". "Vuetify" est un ensemble de composant html+css+javaScript respectant la notion de Material Design de Google (boutons, bandeau, menus déroulants, ...). "Router" est le module Vue pour la gestions des URLs. Il s'agit de code javaScript.

## Django
Django est un web framework codé en python3. Les urls sont géré par le script url.py. Pour chaque url, ce script appelle une fonction dans views.py générant la page html à renvoyer

## l'api Flask
Flask est un web server minimaliste codé en python3. Notre api factice représente les machines à laver dans un grand objet Json. Elle nous permet de renvoyer cet objet Json, ou les information d'une machine particulière via son identifiant, de modifier notre Json via des requètes afin de changer l'état par défaut des machines à laver et d'y rajouter ou d'y enlever des machines à laver.

---


## Utilisateur

### [ipFront]/
Il s'agit de la page d'accueil du site. Elle présente un bandeau déroulant permettant d'accèder au pages **/laveries** et **/auth**. Lorsque les composants de ce menu déroulant sont cliqué ils appellent la méthode javaScript **redirectTo** avec en argument le titre de l'élément cliqué. RedirectTo importe l'ensemble des routes géré par "router", défini dans index.js. "router" utilise le module "Router" de Vue pour charger les pages avec l'url passé en paramètre.

### [ipFront]/laveries
Cette page correspond au fichier Laveries.vue. Il y a un bouton par laverie. Lorsqu'ils sont cliqués ils appellent la méthode **redirectTo** qui est un script javaScript. redirectTo utilise le router de index.js pour charger la page /laveries/'key' où key est l'identifiant de laverie correspondant (B,D,F,...)

### [ipFront]/laveries/'key'
Cette page est similaire pour tout les identifiants de laveries (B,D,F,...). Elles ne sont pas généré a partir d'un template, il s'agit de 7 fichiers .vue différents mais construit de manière très similaire. Cette solution très statique a été choisi car il est très peut probable qu'il y ai besoin de rajouter ou supprimer des laveries entière, ni que le nombre de laveries devienne très important et nécessite des pages généré dynamiquement.

Cette page contient des menus déroulats Vuetify pour réaliser la réservation d'une machine à laver à une certaine heure, et vérifier la disponibilité d'une machine donnée. Cette fonctionalité n'est pas encore implémenté. Le bouton fait appel a la méthode javaScript **verifierDisponibilite** qui renvoit actuellement un message d'erreur.

Cette page contient également un bouton permettant de "voir les machines". Il fait appel à la méthode javaScript **showMachines**. Cette méthode utilise axios pour faire une requête au backend a l'url **[ipBackend]/machine/info/'batiment'**. Les données reçus au format json sont affiché dans un champ de texte pour indiquer le nombre de machines disponibles.

#### requête sur [ipBackend]/machine/info/'batiment'
AAAAAA

### [ipFront]/informerProbleme

Cette page permet a un utilisateur de signaler un problème sur une machine a laver. Des champs de texte et des menus déroulants, qui sont des éléments de Vuetify, permettent de rentrer le nom, le batiment, le numéro de machine et une description du problème. Un bouton permet d'envoyer les information. Il fait appel a la méthode **send()**.

Cette méthode send() renvoie un message d'erreur si tout les champs ne sont pas correctement remplis. Si les chammps sont bien remplis elle communique les données au backend a l'aide d'Axios.

Axios envoie un http POST a l'url **[ipBackend]/saveProblem** avec un Json des données récupéré dans les champs.
L'utilisateur est ensuite renvoyé sur la page d'accueil a l'aide de la méthode route.push('/') défini dans index.js.

#### Post sur [ipBackend]/saveProblem
AAAAAA

## Administrateur

### [ipFront]/auth
Cette page présente deux champs de texte Vuetify fait par défaut pour l'authentification qui permettent de rentrer nom d'utilisateur et mot de passe.
La méthode **login()** permet de vérifier si les données rentré sont complète et correctement formatté (taille du password, caractères interdits,...). Elle envoie ensuite un http POST au backend a l'aide d'axios à l'adresse **[ipBackend]/auth/** avec l'identifiant et le mot de passe de l'utilisateur.

#### Post sur [ipBackend]/auth
AAAAAA

### [ipFront]/admin
Cette page permet d'accédder au pages d'administration des laveries décrites ci-dessous. Elle possède juste 2 hyperliens vers les pages **[ipBackend]/laveries/controler** et **[ipBackend]/laveries/problemes**. Un script javaScript vérifie si l'utilisateur possède le token signifiant qu'il est logué sur une session valide. Si l'utilisateur n'en possède pas il est redirigé vers la page d'authentification **[ipFront]/auth**

## Page administrateur géré par Django
Ces pages sont destiné aux administrateur des laveries. On a choisi d'utiliser de simple page html plutot que de les intégré a l'application Vue. Elle ne sont pas Material Design. Ce choix a été fait car ces pages ne sont pas visible par les utilisateurs et que cela nous permet d'en laisser la gestion a notre backend Django. Ceci nous facilite la tache pour la manipulation des bases de données des laveries et des problèmes en cours car on n'a plus besoin de faire des requêtes entre notre frontend et notre backend via axios.

### [ipBackend]/laveries/controler
Cette page statique correspond au fichier controlerMachine.html. Elle contient 3 champs permettant de renseigner quelle action (allumer ou éteindre) un administrateur souhaite effectué sur quelle machine dans quelle laverie. Un bouton lance un script faisant une requête à l'adresse **[ipBackend]/laveries/controler/[laveries]/[machine]/[comande]**
#### Requête sur [ipBackend]/saveProblem
AAAAAA

### [ipBackend]/laveries/problemes
Cette pages est généré a partir du template html probleme.html. La base de données des problèmes est lue dans la méthode **probleme(request)** définie dans views.py et appellé par urls.py. Pour chaque problème non traité dans la base de données un hyperliens est créé indiquant la date du problème, le batiment dans lequel il est et son statut. L'url vers lequel il pointe est **[ipBackend]/laveries/problemes/[probleme_id]/**

### [ipBackend]/laveries/problemes/[probleme_id]/
Cet url dynamique génére une page html a partir du template detailProbleme.html. L'url est géré par urls.py et appelle la fonction **detail(request, probleme_id)** de views.py. Cette méthode utilise la méthode de django get_object_or_404 pour récupérer les information relative a ce problème s'il existe. S'il n'existe pas l'administrateur et renvoyer vers une page d'erreur 404.
La page généré affiche la description du problème ainsi que 2 boutons : accepter ou refuser.
