from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def cadastro(request):
    #return HttpResponse("funcionando")
    return render(request, 'cadastro.html')