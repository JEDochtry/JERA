from django.http import HttpResponse
from django.template import loader
from .models import MENU
from .models import Category

def menu2(request):
  mymembers = MENU.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mymembers = MENU.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def landing(request):
  template = loader.get_template('landing.html')
  return HttpResponse(template.render())

def menu(request):
    categories = Category.objects.prefetch_related('items').all()
    template = loader.get_template('menu.html')
    context = {'categories': categories}
    return HttpResponse(template.render(context, request))