from flask import Flask
from flask_restful import Api, Resource, reqparse
import sys

app = Flask(__name__)
api = Api(app)

""" Les machines par défaut, là y'a que des exemples un peu bateau niveau contenu, même si les paramètres sont bons"""
users = [
    {
        "heures":    "255",
        "etat":      "on",
        "number":    "55-115151626",
        "modele":    "PT7135 C Vario",
        "fabricant": "Miele",
        "batiment":  "B",
        "id": "6",
        "type":  "Seche"
    },
    {
        "heures":    "256",
        "etat":      "on",
        "number":    "00-096119270",
        "modele":    "PW 5105 LP OB",
        "fabricant": "Miele",
        "batiment":  "B",
        "id": "1",
        "type":  "Lave"
    },
    {
        "heures":    "257",
        "etat":      "on",
        "number":    "56-114982356",
        "modele":    "PW 6065 LP",
        "fabricant": "Miele",
        "batiment":  "B",
        "id": "2",
        "type":  "Lave"
    },
    {
        "heures":    "258",
        "etat":      "on",
        "number":    "56-114982355",
        "modele":    "PW 6065 LP",
        "fabricant": "Miele",
        "batiment":  "B",
        "id": "3",
        "type":  "Lave"
    },
    {
        "heures":    "259",
        "etat":      "on",
        "number":    "65-125593436",
        "modele":    "PW 6065 LP",
        "fabricant": "Miele",
        "batiment":  "B",
        "id": "3_bis",
        "type":  "Lave"
    },
    {
        "heures":    "260",
        "etat":      "on",
        "number":    "56-114982358",
        "modele":    "PW 6065 LP",
        "fabricant": "Miele",
        "batiment":  "B",
        "id": "4",
        "type":  "Lave"
    },
    {
        "heures":    "261",
        "etat":      "on",
        "number":    "62-124608263",
        "modele":    "PW 6065 LP",
        "fabricant": "Miele",
        "batiment":  "B",
        "id": "5",
        "type":  "Lave"
    },
    {
        "heures":    "262",
        "etat":      "on",
        "number":    "40-096064666",
        "modele":    "PT7135 C Vario",
        "fabricant": "Miele",
        "batiment":  "D",
        "id": "8",
        "type":  "Seche"
    },
    {
        "heures":    "263",
        "etat":      "on",
        "number":    "58-125143026",
        "modele":    "PT7135C Vario",
        "fabricant": "Miele",
        "batiment":  "D",
        "id": "9",
        "type":  "Seche"
    },
    {
        "heures":    "264",
        "etat":      "on",
        "number":    "58-125600801",
        "modele":    "PT7135C Vario",
        "fabricant": "Miele",
        "batiment":  "D",
        "id": "12",
        "type":  "Seche"
    },
    {
        "heures":    "265",
        "etat":      "on",
        "number":    "56-114745718",
        "modele":    "PW 6065 LP",
        "fabricant": "Miele",
        "batiment":  "D",
        "id": "11",
        "type":  "Lave"
    },
    {
        "heures":    "266",
        "etat":      "on",
        "number":    "40-095164906",
        "modele":    "PW 6065 Plus LP",
        "fabricant": "Miele",
        "batiment":  "D",
        "id": "2",
        "type":  "Lave"
    },
    {
        "heures":    "267",
        "etat":      "on",
        "number":    "62-125029219",
        "modele":    "PW 6065 Vario LP",
        "fabricant": "Miele",
        "batiment":  "D",
        "id": "3",
        "type":  "Lave"
    },
    {
        "heures":    "268",
        "etat":      "on",
        "number":    "62-125029220",
        "modele":    "PW 6065 Vario LP",
        "fabricant": "Miele",
        "batiment":  "D",
        "id": "4",
        "type":  "Lave"
    },
    {
        "heures":    "269",
        "etat":      "on",
        "number":    "56-114731840",
        "modele":    "PW 6065 LP",
        "fabricant": "Miele",
        "batiment":  "D",
        "id": "5",
        "type":  "Lave"
    },
    {
        "heures":    "270",
        "etat":      "on",
        "number":    "65-125133926",
        "modele":    "PW 6065 Vario LP",
        "fabricant": "Miele",
        "batiment":  "D",
        "id": "6",
        "type":  "Lave"
    },
    {
        "heures":    "271",
        "etat":      "on",
        "number":    "00-120632017",
        "modele":    "PW5105",
        "fabricant": "Miele",
        "batiment":  "D",
        "id": "1",
        "type":  "Lave"
    },
    {
        "heures":    "272",
        "etat":      "on",
        "number":    "40-095174950",
        "modele":    "PW 6065 Plus LP",
        "fabricant": "Miele",
        "batiment":  "D",
        "id": "7",
        "type":  "Lave"
    },
    {
        "heures":    "273",
        "etat":      "on",
        "number":    "60-115199738",
        "modele":    "PW 6065 LP",
        "fabricant": "Miele",
        "batiment":  "E",
        "id": "2",
        "type":  "Lave"
    },
    {
        "heures":    "274",
        "etat":      "on",
        "number":    "60-124558118",
        "modele":    "PW 6065 LP",
        "fabricant": "Miele",
        "batiment":  "E",
        "id": "3",
        "type":  "Lave"
    },
    {
        "heures":    "275",
        "etat":      "on",
        "number":    "40-095161352",
        "modele":    "PW 6065 Plus LP",
        "fabricant": "Miele",
        "batiment":  "E",
        "id": "4",
        "type":  "Lave"
    },
    {
        "heures":    "276",
        "etat":      "on",
        "number":    "55-115173417",
        "modele":    "PT7135 C Vario",
        "fabricant": "Miele",
        "batiment":  "E",
        "id": "1",
        "type":  "Seche"
    },
    {
        "heures":    "277",
        "etat":      "off",
        "number":    "40-095164898",
        "modele":    "PW 6065 Plus LP",
        "fabricant": "Miele",
        "batiment":  "F",
        "id": "1",
        "type":  "Lave"
    },
    {
        "heures":    "278",
        "etat":      "off",
        "number":    "62-124848143",
        "modele":    "PW 6065 Vario LP",
        "fabricant": "Miele",
        "batiment":  "F",
        "id": "2",
        "type":  "Lave"
    },
    {
        "heures":    "279",
        "etat":      "off",
        "number":    "60-115199739",
        "modele":    "PW 6065 LP",
        "fabricant": "Miele",
        "batiment":  "F",
        "id": "4",
        "type":  "Lave"
    },
    {
        "heures":    "280",
        "etat":      "off",
        "number":    "58-124855945",
        "modele":    "PT7135 C Vario",
        "fabricant": "Miele",
        "batiment":  "F",
        "id": "3",
        "type":  "Seche"
    },
    {
        "heures":    "281",
        "etat":      "off",
        "number":    "60-124558115",
        "modele":    "PW 6065 LP",
        "fabricant": "Miele",
        "batiment":  "G-J",
        "id": "4",
        "type":  "Lave"
    },
    {
        "heures":    "282",
        "etat":      "off",
        "number":    "56-114864736",
        "modele":    "PW 6065 LP",
        "fabricant": "Miele",
        "batiment":  "G-J",
        "id": "3",
        "type":  "Lave"
    },
    {
        "heures":    "283",
        "etat":      "off",
        "number":    "56-114839162",
        "modele":    "PW 6065 LP",
        "fabricant": "Miele",
        "batiment":  "G-J",
        "id": "2",
        "type":  "Lave"
    },
    {
        "heures":    "284",
        "etat":      "off",
        "number":    "58-125143023",
        "modele":    "PT7135 C Vario",
        "fabricant": "Miele",
        "batiment":  "G-J",
        "id": "1",
        "type":  "Seche"
    },
    {
        "heures":    "285",
        "etat":      "off",
        "number":    "56-115144886",
        "modele":    "PW 6065 LP",
        "fabricant": "Miele",
        "batiment":  "H",
        "id": "4",
        "type":  "Lave"
    },
    {
        "heures":    "286",
        "etat":      "off",
        "number":    "65-125489107",
        "modele":    "PW 6065 Vario LP",
        "fabricant": "Miele",
        "batiment":  "H",
        "id": "3",
        "type":  "Lave"
    },
    {
        "heures":    "287",
        "etat":      "off",
        "number":    "65-125316123",
        "modele":    "PW 6065 Plus LP",
        "fabricant": "Miele",
        "batiment":  "H",
        "id": "2",
        "type":  "Lave"
    },
    {
        "heures":    "288",
        "etat":      "off",
        "number":    "58-124616693",
        "modele":    "PT7135 C Vario",
        "fabricant": "Miele",
        "batiment":  "H",
        "id": "1",
        "type":  "Seche"
    },
    {
        "heures":    "289",
        "etat":      "off",
        "number":    "65-125204290",
        "modele":    "PW 6065 LP",
        "fabricant": "Miele",
        "batiment":  "I",
        "id": "2",
        "type":  "Lave"
    },
    {
        "heures":    "290",
        "etat":      "off",
        "number":    "60-115089995",
        "modele":    "PW 6065 LP",
        "fabricant": "Miele",
        "batiment":  "I",
        "id": "3",
        "type":  "Lave"
    },
    {
        "heures":    "291",
        "etat":      "off",
        "number":    "40-095056811",
        "modele":    "PW 6065 Plus LP",
        "fabricant": "Miele",
        "batiment":  "I",
        "id": "4",
        "type":  "Lave"
    },
    {
        "heures":    "292",
        "etat":      "off",
        "number":    "58-124855946",
        "modele":    "PT7135 C Vario",
        "fabricant": "Miele",
        "batiment":  "I",
        "id": "1",
        "type":  "Seche"
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
        parser.add_argument("batiment")
        parser.add_argument("id")
        parser.add_argument("type")
        args = parser.parse_args()

        for user in users:
            if number == user["number"]:
                return "Machine avec numéro {} existe déjà".format(number), 400
        user = {
            "heures": args["heures"],
            "etat": args["etat"],
            "number": number,
            "modele": args["modele"],
            "fabricant": args["fabricant"],
            "batiment": args["batiment"],
            "id": args["id"],
            "type": args["type"]
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
        parser.add_argument("batiment")
        parser.add_argument("id")
        parser.add_argument("type")
        args = parser.parse_args()

        for user in users:
            if(number == user["number"]):
                user["etat"] = args["etat"]
                user["heures"] = args["heures"]
                user["modele"] = args["modele"]
                user["fabricant"] = args["fabricant"]
                user["batiment"] = args["batiment"]
                user["id"] = args["id"]
                user["type"] = args["type"]
                return user, 200

        user = {
            "heures": args["heures"],
            "etat": args["etat"],
            "number": number,
            "modele": args["modele"],
            "fabricant": args["fabricant"],
            "batiment": args["batiment"],
            "id": args["id"],
            "type": args["type"]
        }

        print('Modif okk', file=sys.stderr)
        users.append(user)

        return user, 201

    """ Exemple d'URL pour supprimer machine de numéro "blabla" : DELETE http://127.0.0.1:5000/machine/blabla """

    def delete(self,number):
        global users
        users = [user for user in users if user["number"] != number]
        return "La machine de numéro {} a été supprimée de la BD".format(number), 200

api.add_resource(User, "/machine/<string:number>")
app.run(debug=True)
