from django.http import HttpResponse
from datetime import datetime
from django.template import loader
import random
from home.models import Familiar


def crear_familiar(request,nombre, apellido):
    
    familiar=Familiar(nombre=nombre,apellido=apellido,edad=random.randrange(1,99),fecha_creacion=datetime.now())
    familiar.save()
    template = loader.get_template('crear_familiar.html')
    template_renderizado=template.render({'familiar': familiar})
    return HttpResponse(template_renderizado)

def ver_familiares(request):
    
    familiares=Familiar.objects.all()
    template = loader.get_template('ver_familiares.html')
    template_renderizado=template.render({'familiares': familiares})
    return HttpResponse(template_renderizado)