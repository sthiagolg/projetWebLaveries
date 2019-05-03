from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

""" Les machines par défaut, là y'a que des exemples un peu bateau niveau contenu, même si les paramètres sont bons"""
users = [
    {
        "heures": "6h/23h",
        "etat": "on",
        "number": "blabla",
        "modele": "jsp",
        "fabricant": "lg"
    },
    {
        "heures": "6h30/22h30",
        "etat": "off",
        "number": "blabla2",
        "modele": "jsp2",
        "fabricant": "samsung"
    }
]

"""On interroge toujours avec le numéro de série, c'est un truc unique identifiant chaque machine"""
class User(Resource):

    """ Exemple d'URL pour récupérer état machine de numéro "blabla" : GET http://127.0.0.1:5000/machine/blabla """

    def get(self,number):
        for user in users:
            if(number == user["number"]):
                return user, 200
        return "Machine not found", 404
        
    """ Exemple d'URL pour créer machine de numéro "blabla", si numéro pas déjà existant bien sûr :
    POST http://127.0.0.1:5000/machine/blabla?modele=ok&fabricant=lg&heures=23&état=on de paramètres
    modele : ok / fabricant : lg / heures : 23 / etat : on """

    def post(self,number):
        parser = reqparse.RequestParser()
        parser.add_argument("etat")
        parser.add_argument("heures")
        parser.add_argument("modele")
        parser.add_argument("fabricant")
        args = parser.parse_args()

        for user in users:
            if number == user["number"]:
                return "Machine avec numéro {} existe déjà".format(number), 400
        user = {
            "heures": args["heures"],
            "etat": args["etat"],
            "number": number,
            "modele": args["modele"],
            "fabricant": args["fabricant"]
        }
        users.append(user)
        return user, 201
       
    """ Exemple d'URL pour modifier état machine de numéro "blabla" : 
    PUT http://127.0.0.1:5000/machine/blabla?modele=ok&fabricant=lg&heures=23&etat=off
    en mettant : modele : ok / fabricant : lg / heures : 23 / etat : off"""

    def put(self,number):
        parser = reqparse.RequestParser()
        parser.add_argument("etat")
        parser.add_argument("heures")
        parser.add_argument("modele")
        parser.add_argument("fabricant")
        args = parser.parse_args()

        for user in users:
            if(number == user["number"]):
                user["etat"] = args["etat"]
                user["heures"] = args["heures"]
                user["modele"] = args["modele"]
                user["fabricant"] = args["fabricant"]
                return user, 200

        user = {
            "heures": args["heures"],
            "etat": args["etat"],
            "number": number,
            "modele": args["modele"],
            "fabricant": args["fabricant"]
        }
        users.append(user)
        return user, 201
        
    """ Exemple d'URL pour supprimer machine de numéro "blabla" : DELETE http://127.0.0.1:5000/machine/blabla """

    def delete(self,number):
        global users
        users = [user for user in users if user["number"] != number]
        return "La machine de numéro {} a été supprimée de la BD".format(number), 200

api.add_resource(User, "/machine/<string:number>")
app.run(debug=True)
