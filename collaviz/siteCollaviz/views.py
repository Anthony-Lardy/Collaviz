from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from siteCollaviz import script

def collaviz(request):
    test ={
        'test': script.func1(),
    }
    if request.method == 'POST' and request.FILES['fichier']:
        myfile = request.FILES['fichier']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        test ={
            'test': filename
        }
        uploaded_file_url = fs.url(filename)
        return render(request, 'siteCollaviz/accueil.html', test)
    return render(request, 'siteCollaviz/accueil.html', test)
