from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from siteCollaviz import classifier

def collaviz(request):

    if request.method == 'POST' and request.FILES['fichier']:
        myfile = request.FILES['fichier']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        classifier.sql_to_csv(filename)
        donnees ={
            'donnees': classifier.nbActionsall("./media/transition.csv", "'Connexion'")
        }
        return render(request, 'siteCollaviz/accueil.html', donnees)
    return render(request, 'siteCollaviz/accueil.html')
