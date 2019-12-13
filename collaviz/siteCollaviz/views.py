from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from siteCollaviz import classifier
from siteCollaviz import file
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
