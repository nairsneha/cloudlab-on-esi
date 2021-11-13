from django.shortcuts import render

# Create your views here.
#
# from django.http import HttpResponse
#
#
# def homePageView(request):
#     return HttpResponse("Hello, World!")

from django.shortcuts import render
import requests


def index(request):
    response = requests.get('https://618857b5057b9b00177f9c43.mockapi.io/esi/esimock').json()
    return render(request, 'index.html', {'response': response})


def nodeCommands(request, id):
    context = {}
    response = requests.get('https://618857b5057b9b00177f9c43.mockapi.io/esi/esimock/:id').json()
    # context['name'] = response.nodeName
    context['response'] = response
    return render(request, 'nodeCommands.html', {'response': response})
