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
    if Start == None or End == None: 
        desp_data, tc_data = 0, 0
    else:
        Start, End = int(Start), int(End)
        tc_data = [tc_data.tiempo for tc_data in qs[Start:End]]
        desp_data = [desp_data.dato for desp_data in qs[Start:End]]
        for x in tc_data:
            for y in desp_data:
                print(f"{x} - {y}")
    chart = get_plot(tc_data, desp_data)
    return render(request, 'homepage/data_viewer.html', {'chart': chart, 'Colector':COLECTOR})

