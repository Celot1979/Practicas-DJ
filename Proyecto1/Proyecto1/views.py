from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render

class Persona():
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self. apellido = apellido

def saludo(request):
    p1= Persona("Profesor Juan", "Diaz")
    #nombre= "Juan"
    #apellido = "Díaz"
    ahora = datetime.datetime.now()
    temas_Curso = ["Plantillas", "Modelos", "formularios", "vistas","Despliegue"]


    return render(request, "Mi Plantilla.html", {"nombre_persona":p1.nombre, "apellidos": p1.apellido, "momento_actual": ahora, "temas":temas_Curso})



#------------------------------------------------------------------------------------------
    #Plantilla heredada


def cursoC(request):
    fecha_actual = datetime.datetime.now()

    return  render(request, "CursoC.html", {"dameFecha": fecha_actual})


#-------------------------------------------------------------------------------------------
def cursoCss(request):
    fecha_actual = datetime.datetime.now()

    return  render(request, "CursoCss.html", {"dameFecha": fecha_actual})


def despedida(request):
    return HttpResponse(" Espero volver a vernos pronto ")

def dameFecha(request):
    fecha_actual=datetime.datetime.now()
    documento = """<html>
         <body>
         <h1>
         Fecha y hora actuales %s 
         </h1>
         </body>
         </html>""" % fecha_actual
    return HttpResponse(documento)

def calculaEdad(request,edad,agno):
    #edadActual = 18

    periodo= agno-2019
    edadFutura=edad+periodo
    documento="<html><body><h2>En el año %s tendrás %s años" %(agno, edadFutura)
    return  HttpResponse(documento)
