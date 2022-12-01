from django.http import HttpResponse
from django.shortcuts import render
from .models import Colector_datos
from .utils import get_plot
# Create your views here.

def template(request):
    return render(request, "homepage/template.html")


def main_view(request):
    COLECTOR = Colector_datos.objects.all().values()
    qs = Colector_datos.objects.all()
    Start = None
    End = None
    Start = request.POST.get('ID_Start')
    End = request.POST.get('ID_End')
    if Start == None: 
        x=0 
    else:
        Start, End = int(Start), int(End)
        x = [x.tiempo for x in qs[Start:End]]
    if End == None:
        y=0
    else:
        Start, End = int(Start), int(End)
        y = [y.dato for y in qs[Start:End]]

    
    chart = get_plot(x,y)
    return render(request, 'homepage/data_viewer.html', {'chart': chart, 'Colector':COLECTOR})

