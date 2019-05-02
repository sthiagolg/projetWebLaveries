PROJET WEB LAVERIES

SITE
(disponible a tous)
-s’authentifier
	-page initiale
		-historique des machines
			(machine)
			(laverie)
			(date)
		-voir les laveries
			(montre les batiments) 
			(note laverie batiment)
			-noter laverie du batiment 
			-voir machine
				(montre les infos en temps reel)
				(voir liste d’attente)
				(informer un probleme)
				(note de la machine)	
				-reserver une machine
				-noter la machine (1-5 etoiles)
								
				
(mode admin)
-s’authentifier
	-page initiale
		-voir les laveries
						
			-batiments	
				(montre les batiments) 
				-voir toutes les machines
				-voir machine
					(montre les infos en temps reel)
					-envoyer commande
						-redémarrer
						-étendre
						-allumer
					-historique des commandes		

		-voir liste de problemes
			(liste les problemes)
			-voir probleme
				(affiche description du probleme)
					-accepter (redonner le jeton)
						(mail automatique a la personne )
						(envoi un mail au bde pour dire de donner un jeton au guy)
					-refuser 
						(ecrire un mail pour justifier)



API MACHINE  - https://codeburst.io/this-is-how-easy-it-is-to-create-a-rest-api-8a25122ab1f3

-send information about the machine
	(heures de fonctionnement)
	(était actuel - on, off)
	(numero de serie, modèle, fabricant)
	
-receive commands 
	(allumer) -> print dans l’ecran que la commande a été reçue 
	(étendre) -> pareil


BASE DE DONNES (gérée par django)

pour l’instant on va utiliser django pour les utilisateurs, mais dans un moment futur ce sera centralisé par le serveur du bde.

-superutilisateur

-utilisateur
	-nom
	-numero VA
	-batiment
	-historique des machines

-batiment	
	-machines
	
-machine
	-historique des utilisateurs et des commandes
	-etat actuel






		

