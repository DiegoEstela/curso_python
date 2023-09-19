from django.http import HttpResponse
from django.template import Template,Context

def mi_vista(request):
    archivo = open(r'C:\Users\destela\Desktop\Diego\proyects\curso_python\9-semana\app\templates\mi_vista.html')
    template = Template(archivo.read())
    archivo.close()

    contexto = Context()

    template_renderizado = template.render(contexto)

    return HttpResponse(template_renderizado)