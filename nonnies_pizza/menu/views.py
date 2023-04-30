from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Pizza
'''
def menu(request):
    template = loader.get_template('menu.html')
    myitems = Item.objects.all().values()

    context = {
        'myitems': myitems,
    }
    return HttpResponse(template.render(context, request))

'''
def menu(request):
    pizzas = Pizza.objects.all()
    context = {
        'pizzas': pizzas
    }
    return render(request, 'menu.html', context)
