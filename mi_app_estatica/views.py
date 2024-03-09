from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#def index(request):
    #my_context = {'username':'Hola a todos'}
    #return render(request, 'primera_app/index.html', context=my_context)
    #return HttpResponse("<h1> HOLA!!! </h1>")


def index(request):
    username = 'Lista de mis intereses'
    intereses = ['PC GAMERS', 'Mantenimiento automotriz', 'Autos clásicos']
    otras_imagenes = ['pcgamer.jpeg','autoclasico.jpg', 'mantenimiento.jpg']
    return render(request, 'primera_app/index.html', {'username': username, 'intereses': intereses, 'otras_imagenes': otras_imagenes})
