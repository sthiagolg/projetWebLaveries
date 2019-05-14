PROJET WEB LAVERIES

	SITE
	(disponible a tous)
	-s’authentifier
		-page initiale
			/*-historique des machines
				(machine)
				(laverie)
				(date)*/
			-voir les laveries
				(montre les batiments) 			
				-voir machine
					(montre les infos en temps reel)				
					(informer un probleme)


	(mode admin)
	-s’authentifier
		-page initiale

			-voir liste de problemes
				(liste les problemes)
				-voir probleme
					(affiche description du probleme)
						-accepter (redonner le jeton)
							(mail automatique a la personne )
							(envoi un mail au bde pour dire de donner un jeton au 													guy)
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

	/*-utilisateur
		-nom
		-numero VA
		-batiment
		-historique des machines*/


	-machine
		-historique des utilisateurs
		-historique de fonctionnement 
		-etat actuel
		-batiment
		-numero de serie
		-numero de la machine
		-fabricant
		-type de machine
		
TODO (mercredi 15 mai):

		faire page laveries belle
		faire form informerProbleme plus beau
		actualiser api pour avoir les types des machines et le numero pour la laveries
		faire interfaace admin en django pour repondre aux problemes
		faire marcher l’authentification pour l’admin
		charger la base de donnes  django avec les machines api (atomatique?)
		afficher les etats des machines en temps reel






		

