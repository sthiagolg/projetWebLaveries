# Documentation technique "Lavos - plateforme de laverie en ligne de l'INSA Lyon"

Ce site est construit avec Vue pour l'interface utilisateur (frontend) et Django pour la gestion de base de données et la communication avec l'api des machines à laver de l'INSA (backend). Axios, un module javaScript, est utilisé du côté Vue pour faire des requêtes sur le backend Django.

Le backend en Django questionne actuellement une api factice codée en python avec Flask simulant les données des machines à laver. En effet, le travail de récupération des données des machines à laver, leur traitement et présentation via une api sort du cadre de ce projet et sera réalisé par le Clubelek en partenariat avec le BDE de l'INSA de Lyon.

## Vue
Les modules de Vue utilisés sont "Vuetify" et "router". "Vuetify" est un ensemble de composants html+css+javaScript respectant la notion de Material Design de Google (boutons, bandeau, menus déroulants, ...). "Router" est le module Vue pour la gestions des URLs. Il s'agit de code javaScript.

De plus, pour toutes les pages d'url **[ipFront]**, on charge une page html nommée index.html contenant les logos de l'INSA, des laveries (que l'on a créé) ainsi que du BDE.
Ceux-ci sont présents sur toutes ces pages en tant qu'en-tête et renvoient respectivement au site de l'INSA, à la page home de ce site ainsi qu'au site du BDE.

## Django
Django est un web framework codé en python3. Les urls sont gérés par le script url.py. Pour chaque url, ce script appelle une fonction dans views.py générant la page html à renvoyer

## L'api Flask
Flask est un web server minimaliste codé en python3. Notre api factice représente les machines à laver dans un grand objet Json, avec leurs caractéristiques, soit leur numéro de série, bâtiment, nombre d'heures de fonctionnement, fabricant, modèle, numéro dans la laverie, type (sèche-linge lave-linge) ainsi qu'enfin l'état actuel (éteint, allumé, en panne ou en cours de fonctionnement).
Elle nous permet de renvoyer cet objet Json, ou les informations d'une machine particulière via son identifiant, de modifier notre Json via des requêtes afin de changer l'état par défaut des machines à laver et d'y rajouter ou d'y enlever des machines à laver.

---


## Utilisateur

### [ipFront]/
Il s'agit de la page d'accueil du site. Elle présente un bandeau déroulant permettant d'accèder aux pages **/laveries**, **/informerProbleme**, **/auth** et **/About**. Lorsque les composants de ce menu déroulant sont cliqués ils appellent la méthode javaScript **redirectTo** avec en argument le titre de l'élément cliqué.
RedirectTo importe l'ensemble des routes gérées par "router", ceci étant défini dans index.js. "router" utilise le module "Router" de Vue pour charger les pages avec l'url passé en paramètre.

Cette page affiche également des articles rédigés par l'admin correspondant aux dernières nouvelles de la laverie, ceux-ci pouvant être une panne déclarée, une réparation effectuée, une ou plusieurs nouvelles machines amenées, etc.

### [ipFront]/auth
Cette page présente deux champs de texte Vuetify créés par défaut pour l'authentification qui permettent de rentrer le nom d'utilisateur et mot de passe. Elle sert à ce que l'administrateur puisse accéder aux pages qui lui sont réservées.
La méthode **login()** permet de vérifier si les données rentrées sont complètes et correctement formatées (taille du password, caractères interdits,...). Elle envoie ensuite un http POST au backend à l'aide d'axios à l'adresse **[ipBackend]/auth/** avec l'identifiant et le mot de passe de l'utilisateur.

### [ipFront]/laveries
Cette page correspond au fichier Laveries.vue. Il y a un bouton par laverie. Lorsqu'ils sont cliqués ils appellent la méthode **redirectTo** qui est un script javaScript. redirectTo utilise le router de index.js pour charger la page /laveries/'key' où key est l'identifiant de laverie correspondant (B,D,F,...)
Egalement, dans cette page on trouve sous les boutons une image modifiée du campus où on signale la localisation de chaque laverie.

### [ipFront]/laveries/'key'
Cette page est similaire pour tous les identifiants de laveries (B,D,F,...). Elles ne sont pas générées a partir d'un template, il s'agit de 7 fichiers .vue différents mais construits de manière très similaire. Cette solution très statique a été choisie car il est très peu probable qu'il y ait besoin de rajouter ou supprimer des laveries entières, ni que le nombre de laveries devienne très important et nécessite des pages générées dynamiquement.

Cette page contient des menus déroulants Vuetify pour vérifier la disponibilité d'une machine donnée, voire plus tard réserver une machine à laver à une certaine heure. Cette fonctionalité n'est pas encore implémentée car on a pas encore accès aux bases de données du BDE permettant d'identifier l'utilisateur.
Le bouton déjà créé, "Show Machines", fait appel à la méthode javaScript **verifierDisponibilite** qui renvoie actuellement un message d'erreur.

Enfin, cette page contient également un bouton permettant de voir les machines disponibles actuellement, nommé très justement "Show Machines Available Now". Il fait appel à la méthode javaScript **showMachines()**. Cette méthode utilise axios pour faire une requête au backend à l'url **[ipBackend]/machine/info/'batiment'**. Les données reçues au format json sont affichées dans un champ de texte pour indiquer le nombre de machines disponibles.

#### Requête sur [ipBackend]/machine/info/'batiment'
Cet url fait appel à la méthode **getMachine()** de views.py. Cette méthode renvoie le nombre de sèche-linges et de lave-linges disponibles. Pour ça, il récupère toutes les machines correspondant au bâtiment demandé dans la base de données correspondante. Puis pour chaque machine, il appelle la méthode *regarderMachineApi2*.
Cette méthode fait une requête à l'api sur l'url **[ipApi]/machine/[number]** pour récupérer les donnèes actuelles des machines et les mettre à jour dans sa base de données. Enfin, une requête à la base de données des machines est réalisée pour sélectionner uniquement les lave-linges et sèche-linges disponibles. Ils sont comptés et on retourne ces 2 nombres au format Json.

### [ipFront]/informerProbleme

Cette page permet à un utilisateur de signaler un problème sur une machine à laver. Des champs de texte et des menus déroulants, qui sont des éléments de Vuetify, permettent de rentrer le nom, le batiment, le numéro de machine et une description du problème.
On a fait en sorte que seuls les numéros de machines disponibles dans le bâtiment sélectionné apparaissent. Un bouton permet ainsi d'envoyer les informations. Il fait appel à la méthode **send()**.

Cette méthode send() renvoie un message d'erreur si tous les champs ne sont pas correctement remplis. Si les champs sont bien remplis, elle communique les données au backend à l'aide d'Axios. Ce problème sera disponible pour l'admin à la page d'url **[ipBackend]/laveries/problemes**.

Axios envoie un http POST à l'url **[ipBackend]/saveProblem** avec un Json rempli des différentes données récupérées dans les champs.
L'utilisateur est ensuite renvoyé sur la page d'accueil à l'aide de la méthode route.push('/') définie dans index.js.

#### Post sur [ipBackend]/saveProblem
Cet url appelle la méthode **saveProblem()** de views.py. Cette méthode récupère le Json passé par le http POST et ajoute dans la base de données des problèmes en cours les données passées de cette manière.
Celle-ci reçoit ainsi l'identité de l'utilisateur, la machine sur laquelle il y a un problème, le bâtiment où il y a ce problème, la description de celui-ci et si celui-ci est accepté, refusé ou en attente. Il renvoie un Json avec un message de validation.

### [ipFront]/About
Cette page contient un descriptif du projet en quelques lignes, ainsi qu'un lien vers cette page html décrivant plus en détail chaque page et requête impliquée dans le fonctionnement du site.

## Administrateur

#### Post sur [ipBackend]/auth
La gestion de cet url est faite par une méthode par défaut de django **obtain_jwt_token()** du package **rest_framework_jwt.views**. Il permet de délivrer un cookie d'authentification (token) si l'utilisateur et le mot de passe sont corrects.

### [ipFront]/admin
Cette page permet d'accéder aux pages d'administration des laveries décrites ci-dessous. Elle possède juste 3 hyperliens vers les pages **[ipBackend]/laveries/controler**, **[ipBackend]/laveries/problemes**, **[ipBackend]/postCreate**.
Un script javaScript vérifie en permanence si l'utilisateur possède le token signifiant qu'il est logué sur une session valide. Si l'utilisateur n'en possède pas il est automatiquement redirigé vers la page d'authentification **[ipFront]/auth**.

## Page administrateur géré par Django
Ces pages sont destinées aux administrateurs des laveries. On a choisi d'utiliser de simples pages html plutôt que de les intégrer à l'application Vue. Elle ne sont pas Material Design. Ce choix a été fait car ces pages ne sont pas visibles par les utilisateurs et que cela nous permet d'en laisser la gestion à notre backend Django.
Ceci nous facilite la tâche pour la manipulation des bases de données des laveries et des problèmes en cours car on n'a plus besoin de faire des requêtes entre notre frontend et notre backend via axios.

### [ipBackend]/laveries/controler
Cette page statique correspond au fichier controlerMachine.html. Elle contient 3 champs permettant de renseigner quelle action (allumer ou éteindre) un administrateur souhaite effectuer sur quelle machine dans quelle laverie. Un bouton lance un script faisant une requête à l'adresse **[ipBackend]/laveries/controler/[laveries]/[machine]/[commande]**

#### Requête sur [ipBackend]/saveProblem
Cet url appelle la méthode **sendCommand()** de views.py qui est protégé par un @login_required. Elle ne peut pas être accédée sans le cookie d'authentification (token).
Elle met à jour l'état de la machine sur la base de données des machines et envoie la demande de changement d'état à l'api pour la machine concernée avec un http PUT à l'url **[ipApi]/[machine]/[numeroSerie]**. Elle retourne un message d'erreur si la machine n'existe pas, et un message de confirmation si la machine existe et que la requête a donc été réalisée.

### [ipBackend]/laveries/problemes
Cette page est générée à partir du template html probleme.html. La base de données des problèmes est lue dans la méthode **probleme(request)** définie dans views.py et appellé par urls.py. Pour chaque problème non traité dans la base de données un hyperlien est créé indiquant la date du problème, le bâtiment dans lequel il est et son statut (accepté, refusé ou non traité). L'url vers lequel il pointe est **[ipBackend]/laveries/problemes/[probleme_id]/**

### [ipBackend]/laveries/problemes/[probleme_id]/
Cet url dynamique génère une page html à partir du template detailProbleme.html. L'url est géré par urls.py et appelle la fonction **detail(request, probleme_id)** de views.py. Cette méthode utilise la méthode de django get_object_or_404 pour récupérer les information relatives à ce problème s'il existe. S'il n'existe pas l'administrateur est renvoyé vers une page d'erreur 404.
La page générée affiche la description du problème ainsi que 2 boutons : accepter ou refuser.
