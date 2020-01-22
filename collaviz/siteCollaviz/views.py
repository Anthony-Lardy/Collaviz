from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from siteCollaviz import classifier
from siteCollaviz import file
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from siteCollaviz.forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt

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
    elif request.method == 'POST' and 'username' in request.POST and 'email' in request.POST:
        register(request)
    elif request.method == 'POST' and 'username' in request.POST and 'password' in request.POST:
        login_user(request)
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
            user = authenticate(request, username=username, password=raw_password, email=email)
            login(request, user)
            return redirect('siteCollaviz/accueil.html')
        else:
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
            return render(request, 'siteCollaviz/accueil.html', {'form': form})
    else:
        form = AuthenticationForm()
    return render(request, 'siteCollaviz/accueil.html', {'form': form})


@csrf_exempt
def logout_user(request):
    logout(request)
    return redirect('siteCollaviz/accueil.html')
