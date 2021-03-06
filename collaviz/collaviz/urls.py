"""collaviz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
1. Add an import:  from my_app import views
2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
1. Add an import:  from other_app.views import Home
2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
1. Import the include() function: from django.urls import include, path
2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_view
from django.urls import path
from siteCollaviz import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('collaviz', views.collaviz),
    path('mappingDonnees', views.mappingDonnees),
    path('validerParams', views.validerParams),
    path('validerParamsCamembert', views.validerParamsCamembert),
    path('validerParamsBarSimple', views.validerParamsBarSimple),
    path('validerParamsComplexes', views.validerParamsComplexes),
    path('register', views.register),
    path("logout_user", views.logout_user),
    path("login_user", views.login_user),
    path("separateur", views.separateur),
    path("fichierMapping", views.fichierMapping),
    path("getUsers", views.getUsers),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
