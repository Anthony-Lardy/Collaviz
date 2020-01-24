from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from siteCollaviz import classifier
from siteCollaviz import file
from siteCollaviz import mapping
from siteCollaviz import graph
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import numpy as np


def collaviz(request):

    if request.method == 'POST' and request.FILES['fichier']:
        folder='media/tmp/'
        myfile = request.FILES['fichier']
        fs = FileSystemStorage(location=folder)
        filename = fs.save(myfile.name, myfile)
        classifier.sql_to_csv(filename)
        donnees ={
            'donnees': classifier.nbActionsall("./media/tmp/transition.csv", "'Connexion'"),
            'file': file.findallfile("./media/tmp/")
        }
        return render(request, 'siteCollaviz/accueil.html', donnees)
    return render(request, 'siteCollaviz/accueil.html')

@csrf_exempt
def mappingDonnees(request):
    if request.is_ajax() and request.method == 'POST':
        mapping.mapping(request.POST['fichier'], request.POST['utilisateur'], request.POST['date'], request.POST['heure'],
        request.POST['titre'], request.POST['attribut'], request.POST['repondre'], request.POST['poster'], request.POST['forum'],
         request.POST['message'], request.POST['parent'])
    return render(request, 'siteCollaviz/accueil.html')

@csrf_exempt
def validerParams(request):
        if request.is_ajax() and request.method == 'POST':
            array_data = request.POST['utilisateurs']
            utilisateurs = json.loads(array_data)
            data = graph.actionParTemps(utilisateurs, request.POST.get('actions'), request.POST['dateDeb'], request.POST['dateFin'])
            return JsonResponse(data, safe=False)
        return render(request, 'siteCollaviz/accueil.html')
