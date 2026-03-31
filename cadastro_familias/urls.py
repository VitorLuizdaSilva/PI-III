from django.urls import path
from django.http import HttpResponse
from cadastro_familias.views import cadastro

urlpatterns = [
    path('cadastro/', cadastro)
]