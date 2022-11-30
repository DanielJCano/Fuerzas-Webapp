from django.http import HttpResponse
from django.shortcuts import render
from .models import Colector_datos
from .utils import get_plot
# Create your views here.


def index(request):

    return render(request, "homepage/data_viewer.html")


def template(request):
    return render(request, "homepage/template.html")


def main_view(request):
    qs = Colector_datos.objects.all()
    x = [x.tiempo for x in qs]
    y = [y.dato for y in qs]
    chart = get_plot(x,y)
    return render(request, 'homepage/data_viewer.html', {'chart': chart})

