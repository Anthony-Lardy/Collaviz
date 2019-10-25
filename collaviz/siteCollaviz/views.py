from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def collaviz(request):
    if request.method == 'POST' and request.FILES['fichier']:
        myfile = request.FILES['fichier']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'siteCollaviz/accueil.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'siteCollaviz/accueil.html')
