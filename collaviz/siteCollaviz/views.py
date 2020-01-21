from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from siteCollaviz import classifier
from siteCollaviz import file
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from siteCollaviz.forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def collaviz(request):
    if request.method == 'POST' and 'fichier' in request.POST:
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
    elif request.method == 'POST' and 'username' in request.POST:
        register(request)
    return render(request, 'siteCollaviz/accueil.html')

def register(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        email = form.cleaned_data.get('email')
        user = authenticate(request, username=username, password=raw_password)
        login(request, user)
        return redirect('siteCollaviz/accueil.html')
    else:
        print(form.errors.as_data())
    return render(request, 'siteCollaviz/accueil.html', {'form': form})
