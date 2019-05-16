
from django.shortcuts import render, get_object_or_404,redirect
import requests
from datetime import datetime
from machine.models import Machine
from machine.models import Probleme
from django.http import JsonResponse
from django.contrib.auth.models import Permission, User
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest, request
import httplib2
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
import urllib
import urllib.parse
import json
from django.contrib.auth.decorators import login_required
from rest_framework.status import (
HTTP_200_OK

)

# Create your views here.
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def regarderMachineApi2(number): #on doit mettre http://127.0.0.1:8000/machine/blabla

    """data = {
        "heures": "12",
        "etat": "On",
        "number": "azer",
        "modele": "ty",
        "fabricant": "vamo"
    }
    body = urllib.parse.urlencode(data)"""
    item=""
    try:
        h = httplib2.Http()
        #number = "blabla"
        resp, content = h.request("http://127.0.0.1:5000/machine/"+number, method="GET")

        my_json = content.decode('utf8').replace("'", '"')
        print(my_json)
        data = json.loads(my_json)
        heures = data["heures"]
        etat = data["etat"]
        number = data["number"]
        modele = data["modele"]
        fabricant = data["fabricant"]
        batiment = data["batiment"]
        identifiant = data["id"]
        type = data["type"]



        try:
            machine = get_object_or_404(Machine, number=number)

            dernierEtat = machine.etat

            item = machine.etat

            #ajoute un nouveau etat a machine, a changer apreees
            machine.etat = etat
            machine.historique = machine.historique+"\t"+str(dernierEtat)
            machine.save()
        except:

            maquinaNova = Machine.objects.create(heures=heures, etat=etat, number=number, modele=modele,
                                                 fabricant=fabricant, batiment=batiment,type=type,identifiant=identifiant)
            maquinaNova.save()

    except:
        print("machine n'existe pas...")


    #return render(request, 'test.html',{'item':item})


def regarderMachineApi(request,number): #on doit mettre http://127.0.0.1:8000/machine/blabla

    """data = {
        "heures": "12",
        "etat": "On",
        "number": "azer",
        "modele": "ty",
        "fabricant": "vamo"
    }
    body = urllib.parse.urlencode(data)"""
    item=""
    try:
        h = httplib2.Http()
        #number = "blabla"
        resp, content = h.request("http://127.0.0.1:5000/machine/"+number, method="GET")

        my_json = content.decode('utf8').replace("'", '"')
        print(my_json)
        data = json.loads(my_json)
        heures = data["heures"]
        etat = data["etat"]
        number = data["number"]
        modele = data["modele"]
        fabricant = data["fabricant"]
        batiment = data["batiment"]
        identifiant = data["id"]
        type = data["type"]



        try:
            machine = get_object_or_404(Machine, number=number)

            dernierEtat = machine.etat

            item = machine.etat

            #ajoute un nouveau etat a machine, a changer apreees
            machine.etat = etat
            machine.historique = machine.historique+"\t"+str(dernierEtat)
            machine.save()
        except:

            maquinaNova = Machine.objects.create(heures=heures, etat=etat, number=number, modele=modele,
                                                 fabricant=fabricant, batiment=batiment,type=type,identifiant=identifiant)
            maquinaNova.save()

    except:
        print("machine n'existe pas...")


    return render(request, 'test.html',{'item':item})


def getMachines(request,batiment):



    #item = Machine.objects.get(number=number)

    #return render(request, 'test.html',{'item':item })
    #return HttpResponse("Here's the text of the Web page.")
    #return item.etat



    machines = Machine.objects.filter(batiment=batiment)

    listMachines  = []



    #print(machines[0])
    for i in range(len(machines)):
        #print(machines[i])
        regarderMachineApi2(str(machines[i]))
        #listMachines.append(str(machines[i]))

    laves = Machine.objects.filter(batiment=batiment, type='Lave', etat='on')
    seches = Machine.objects.filter(batiment=batiment, type='Seche', etat='on')

    nbLaves = laves.__len__()
    nbSeches = seches.__len__()

    print(listMachines)

    #print(item.etat)
    #return Response({'item': item.etat}, status=HTTP_200_OK)
    return JsonResponse({'lave': str(nbLaves),'seche':str(nbSeches)})

def index(request):
    if request.user.is_authenticated:
        print("c bon")
        return render(request, 'index.html')
    else:
        return HttpResponse("Nao autentificado")



def seeLaveries(request,numLaveries):
    machines= Machine.objects.filter(batiment=numLaveries)
    return render(request,'B.html',{'machines':machines})

@csrf_exempt
def saveProblem(request):

    #item = Machine.objects.get(number=number)

    #return render(request, 'test.html',{'item':item })
    #return HttpResponse("Here's the text of the Web page.")
    #return item.etat

    content = json.loads(request.body)

    name = content["name"]
    machine = content["machine"]
    batiment = content["batiment"].upper()
    description = content["description"]
    resolution = "NT"


    novoProblema = Probleme.objects.create(nom=name,machine=machine,batiment=batiment,description=description,resolution=resolution)
    novoProblema.save()

    print(content)


    #return Response({'item': item.etat}, status=HTTP_200_OK)
    return JsonResponse({'response':'Votre problème a été envoyé et il sera pris en compte bientot!'})


@login_required(login_url='http://127.0.0.1:8080/Auth')
#@login_required()
def problemes(request):

    problemes= Probleme.objects.filter(resolution='NT')
    allproblemes = Probleme.objects

    return render(request, 'problemes.html', {'problemes': problemes, 'allproblemes':allproblemes})

def detail(request, probleme_id):
    detail = get_object_or_404(Probleme, pk=probleme_id)
    return render(request, 'detailProbleme.html', {'probleme': detail})

@login_required(login_url='http://127.0.0.1:8080/Auth')
#@login_required()
def repondreProbleme(request , probleme_id, status):
    #content = json.loads(request.body)

    print(probleme_id,status)

    if status == "accepté":
        probleme = Probleme.objects.get(pk=probleme_id)
        probleme.resolution = "A"
        probleme.save()

    if status == "refusé":
        probleme = Probleme.objects.get(pk=probleme_id)
        probleme.resolution = "N"
        probleme.save()


    #return HttpResponse("Problème de numero "+str(probleme_id)+" : "+str(status))
    problemes = Probleme.objects.filter(resolution='NT')
    allproblemes = Probleme.objects
    return render(request, 'problemes.html', {'problemes': problemes, 'allproblemes':allproblemes})

def pageIniciale(request):

    return HttpResponseRedirect("http://127.0.0.1:8080")

@login_required(login_url='http://127.0.0.1:8080/Auth')
def controlerMachine(request):

    return render(request,'controlerMachine.html')

@login_required(login_url='http://127.0.0.1:8080/Auth')
def sendCommand(request,laverie,machine,commande):

    cmd = ''

    if commande == "Allumer":
        cmd = 'on'

    if commande == "Etendre":
        cmd = 'off'

    try:
        maquina = Machine.objects.get(batiment=laverie,identifiant=machine)
        numeroSerie = maquina.number
        type = maquina.type
        heures = maquina.heures
        modele=maquina.modele
        fabricant=maquina.fabricant
        batiment=maquina.batiment
        identifiant=maquina.identifiant

        responseBody={
                'heures': heures,
                'etat': cmd,
                'number': numeroSerie,
                'modele': modele,
                'fabricant': fabricant,
                'batiment': batiment,
                'id': identifiant,
                'type': type,
                }


        response = requests.put('http://127.0.0.1:5000/machine/'+str(numeroSerie),data=responseBody)
        #resp = response.json()
        #machine = Machine.objects.get(number=numeroSerie)
        #machine.etat = cmd
        #machine.save()

        print(response)


        return HttpResponse("Machine  "+machine+"  "+str(type)+"  "+laverie +"  ("+str(maquina)+") -> "+commande+" OK!")
    except:
        return HttpResponse("Machine n'existe pas!")

