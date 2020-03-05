from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from siteCollaviz import classifier
from siteCollaviz import file
from siteCollaviz import mapping
from siteCollaviz import actionParTemps
from siteCollaviz import actionsParTemps
from siteCollaviz import tempsReponseMoyen
from siteCollaviz import nbReponsesAuxAutres
from siteCollaviz import actionsUser
from siteCollaviz import actionUsers
from siteCollaviz import nbReponsesDesAutres
from siteCollaviz import calculIndicateurs
from siteCollaviz import gestionDate
from siteCollaviz import cellDupli
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import numpy as np
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from siteCollaviz.forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
import os
import time

@csrf_exempt
def collaviz(request):
    folder= 'media/' + request.user.username + "/"
    donnees = {

    }
    print(request.user.username)
    if(request.user.username is not ''):
        donnees = {
            'file' : file.findallfile(folder),
            'mapping': file.findallfile(folder + "mapping/")
        }
    if request.method == 'POST' and 'fichier' in request.FILES:
        myfile = request.FILES['fichier']
        fs = FileSystemStorage(location=folder)
        filename = fs.save(myfile.name, myfile)
        classifier.sql_to_csv(request.user.username, filename)
        donnees = {
            'file' : file.findallfile(folder),
            'mapping': file.findallfile(folder + "mapping/")
        }
        return render(request, 'siteCollaviz/accueil.html', donnees)
    return render(request, 'siteCollaviz/accueil.html', donnees)

@csrf_exempt
def fichierMapping(request):
    folder= 'media/' + request.user.username + "/"
    donnees =  file.findallfile(folder + "mapping/")
    return JsonResponse(donnees, safe=False)

@csrf_exempt
def getUsers(request):
    donnees =  actionParTemps.getUsers(request.user.username, request.POST['file'])
    return JsonResponse(donnees, safe=False)

@csrf_exempt
def mappingDonnees(request):
    folder= 'media/' + request.user.username + "/mapping/"
    fichierNew = file.findallfile(folder)
    fichierOld = file.findallfile(folder)
    if request.is_ajax() and request.method == 'POST':
        mapping.mapping(request.user.username, request.POST['fichier'], request.POST['utilisateur'], request.POST['date'], request.POST['heure'], request.POST['titre'], request.POST['attribut'], request.POST['delai'],
        request.POST['repondre'], request.POST['poster'], request.POST['lecture'], request.POST['connexion'],
        request.POST['forum'], request.POST['message'], request.POST['parent'])
    while fichierOld == fichierNew:
        fichierNew = file.findallfile(folder)
    donnees = {
        'mapping' : file.findallfile(folder),
    }
    return render(request, 'siteCollaviz/accueil.html', donnees)

@csrf_exempt
def separateur(request):
    folder= 'media/' + request.user.username + "/"
    fichierNew = file.findallfile(folder)
    fichierOld = file.findallfile(folder)
    if request.is_ajax() and request.method == 'POST':
        cellDupli.duppliCellulelist(request.user.username, request.POST['fichier'], request.POST['colonne'], request.POST['separateur'])
    while fichierOld == fichierNew:
        print(fichierOld, fichierNew)
        fichierNew = file.findallfile(folder)
    donnees = {
        'file' : file.findallfile(folder),
    }
    return render(request, 'siteCollaviz/accueil.html', donnees)

@csrf_exempt
def validerParams(request):
        if request.is_ajax() and request.method == 'POST':
            array_data = request.POST['utilisateurs']
            utilisateurs = json.loads(array_data)
            data = []
            data.append(actionParTemps.actionParTemps(request.user.username, request.POST['file'], utilisateurs, request.POST.get('actions'), request.POST['dateDeb'], request.POST['dateFin']))
            if(request.POST['dateDeb'] == ""):
                data.append(gestionDate.getFirstDate(request.user.username, request.POST['file']))
            else:
                data.append(request.POST['dateDeb'])
            print(data)
            return JsonResponse(data, safe=False)
        return render(request, 'siteCollaviz/accueil.html')

@csrf_exempt
def validerParamsBarSimple(request):
        if request.is_ajax() and request.method == 'POST':
            array_data = request.POST['utilisateurs']
            utilisateurs = json.loads(array_data)
            fichier = 'media/' + request.user.username + "/mapping/"+request.POST['file']
            data = actionUsers.actionPourUtilisateurs(fichier, request.POST.get('action'), utilisateurs, request.POST['dateDeb'], request.POST['dateFin'])
            return JsonResponse(data, safe=False)
        return (request, 'siteCollaviz/accueil.html')

@csrf_exempt
def validerParamsCamembert(request):
        if request.is_ajax() and request.method == 'POST':
            array_data = request.POST['actions']
            actions = json.loads(array_data)
            fichier = 'media/' + request.user.username + "/mapping/"+request.POST['file']
            data = actionsUser.actionsParUtilisateur(fichier, request.POST['utilisateur'], actions, request.POST['dateDeb'], request.POST['dateFin'])
            return JsonResponse(data, safe=False)
        return render(request, 'siteCollaviz/accueil.html')

@csrf_exempt
def validerParamsComplexes(request):
        if request.is_ajax() and request.method == 'POST':
            tab = []
            fichier = 'media/' + request.user.username + "/mapping/"+request.POST['fichier']
            actions = ["Connexion", "Répondre à un message","Poster un nouveau message"]
            print("actionsParTemps")
            tab.append(actionsParTemps.actionsParTemps(fichier, actions,request.POST['utilisateur'], request.POST['dateDebut'], request.POST['dateFin']))
            tab.append(actionsParTemps.actionsParTempsAll(fichier, actions, request.POST['dateDebut'], request.POST['dateFin']))
            print("indicateurTempsMoyen")
            tab.append(tempsReponseMoyen.indicateurTempsMoyen(fichier, request.POST['utilisateur'], json.loads(request.POST['groupeUsers']), request.POST['dateDebut'], request.POST['dateFin']))
            print(tab[2])
            print("nbReponsesDePersonne")
            tab.append(nbReponsesAuxAutres.nbReponsesDePersonneGroupe(fichier, request.POST['utilisateur'], request.POST['groupeUsers'], request.POST['dateDebut'], request.POST['dateFin']))
            print("nbReponsesParPersonne")
            tab.append(nbReponsesDesAutres.nbReponsesParPersonneGroupe(fichier, request.POST['utilisateur'], request.POST['groupeUsers'], request.POST['dateDebut'], request.POST['dateFin']))
            print("calculsIndicateurs")
            tab.append(calculIndicateurs.calculsIndicateurs(fichier, request.POST['utilisateur'], request.POST['groupeUsers'], request.POST['dateDebut'], request.POST['dateFin']))
            print("calculsNbActions")
            tab.append(calculIndicateurs.calculsNbActions(fichier, json.loads(request.POST['groupeUsers'])))
            if(request.POST['dateDebut'] == ""):
                tab.append(gestionDate.getFirstDate(request.user.username, request.POST['fichier']))
            else:
                tab.append(request.POST['dateDebut'])
            return JsonResponse(tab, safe=False)
        return render(request, 'siteCollaviz/accueil.html')

@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            raw_password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            folder= 'media/' + username + "/"
            os.mkdir(folder)
            folder= 'media/' + username + "/mapping/"
            os.mkdir(folder)
            user = authenticate(request, username=username, password=raw_password, email=email)
            login(request, user)
            return JsonResponse(2, safe=False)
        else:
            messages.error(request, form.errors)
            print(form.errors.as_data())
            return JsonResponse(form.errors.as_json(), safe=False)
    else:
        form = SignUpForm()
    return JsonResponse(2, safe=False)

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username, password = form.cleaned_data['username'], form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
        else:
            print("Formulaire invalide")
            print(form.errors.as_data())
            return JsonResponse(form.errors.as_json(), safe=False)
    else:
        form = AuthenticationForm()
    return JsonResponse(2, safe=False)


@csrf_exempt
def logout_user(request):
    logout(request)
    return render(request, 'siteCollaviz/accueil.html')
