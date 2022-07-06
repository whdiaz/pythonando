from django.shortcuts import render
from django.http import HttpResponse

def cadastro(request):
      return render(request, 'cadastro.html')

def logar(request):
      return HttpResponse('voce esta na pagina de login')      



# Create your views here.
