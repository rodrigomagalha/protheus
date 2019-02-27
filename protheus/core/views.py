from django.http import HttpResponse
from django.shortcuts import render


def load_protheus(request):
    return render(request, 'template/protheus.html')
