from django.shortcuts import render
from django.http import HttpResponse
def cadastro(request):
    print(request.META)
    return render(request,'cadastro.html')