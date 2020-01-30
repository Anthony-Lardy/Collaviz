from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from siteCollaviz import classifier
from siteCollaviz import file
from siteCollaviz import mapping
from siteCollaviz import actionParTemps
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

@csrf_exempt
def collaviz(request):
    print(request.user.username)
    if request.method == 'POST' and 'fichier' in request.FILES:
        folder= 'media/' + request.user.username + "/"
        myfile = request.FILES['fichier']
        fs = FileSystemStorage(location=folder)
        filename = fs.save(myfile.name, myfile)
        classifier.sql_to_csv(request.user.username, filename)
        donnees = {
            'file' : file.findallfile(folder)
        }
        return render(request, 'siteCollaviz/accueil.html', donnees)
    elif request.method == 'POST' and 'username' in request.POST and 'email' in request.POST:
        register(request)
    elif request.method == 'POST' and 'username' in request.POST and 'password' in request.POST:
        login_user(request)
    return render(request, 'siteCollaviz/accueil.html')

@csrf_exempt
def mappingDonnees(request):
    if request.is_ajax() and request.method == 'POST':
        mapping.mapping(request.POST['fichier'], request.POST['utilisateur'], request.POST['date'], request.POST['heure'], request.POST['titre'], request.POST['attribut'], request.POST['delai'],
        request.POST['repondre'], request.POST['poster'], request.POST['connexion'],
        request.POST['forum'], request.POST['message'], request.POST['parent'])
        data = actionParTemps.getUsers()
        return JsonResponse(data, safe=False)
    return render(request, 'siteCollaviz/accueil.html')

@csrf_exempt
def separateur(request):
    if request.is_ajax() and request.method == 'POST':
        cellDupli.duppliCellulelist(request.POST['fichier'], request.POST['colonne'], request.POST['separateur'])
    return HttpResponseRedirect(request.path_info)

@csrf_exempt
def validerParams(request):
        if request.is_ajax() and request.method == 'POST':
            array_data = request.POST['utilisateurs']
            utilisateurs = json.loads(array_data)
            data = actionParTemps.actionParTemps(utilisateurs, request.POST.get('actions'), request.POST['dateDeb'], request.POST['dateFin'])
            return JsonResponse(data, safe=False)
        return render(request, 'siteCollaviz/accueil.html')


@csrf_exempt
def validerParamsComplexes(request):
        if request.is_ajax() and request.method == 'POST':
            fichier = "./media/tmp/"+request.POST['fichier']
            actions = ["Connexion", "Repondre a un message","Poster un nouveau message"]
            data = actionsParTemps.actionsParTemps(fichier, actions,request.POST['utilisateur'], request.POST['dateDebut'], request.POST['dateFin'])
            return JsonResponse(data, safe=False)
        return render(request, 'siteCollaviz/accueil.html')

        
@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            folder= 'media/' + username + "/"
            os.mkdir(folder)
            folder= 'media/' + username + "/mapping/"
            os.mkdir(folder)
            user = authenticate(request, username=username, password=raw_password, email=email)
            login(request, user)
            return redirect('siteCollaviz/accueil.html')
        else:
            messages.error(request, form.errors)
            print(form.errors.as_data())
    else:
        form = SignUpForm()
    return render(request, 'siteCollaviz/accueil.html', {'form': form})

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        print("Putain je suis rentré")
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            print("Formulaire valide incroyable du cul monsieur Potter")
            username, password = form.cleaned_data['username'], form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
        else:
            print("Formulaire invalide")
            print(form.errors)
            messages.error(request, form.errors)
            return render(request, 'siteCollaviz/accueil.html', {'form': form})
    else:
        form = AuthenticationForm()
    return render(request, 'siteCollaviz/accueil.html', {'form': form})


@csrf_exempt
def logout_user(request):
    logout(request)
    return redirect('siteCollaviz/accueil.html')
