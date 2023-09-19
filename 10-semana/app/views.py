from django.http import HttpResponse
from django.template import loader 
from datetime import datetime

def probando_template(request):
    nombre = "Diego"
    apellido = "Estela"
    lista_de_notas = [1,2,3,4,5,6,7]

    diccionario = {"nombre" : nombre, "apellido" : apellido, "hoy": datetime.now(), "notas" : lista_de_notas} # <---- para enviar al contexto

    plantilla = loader.get_template("template1.html")

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)