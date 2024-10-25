from django.views.generic import TemplateView
from django.shortcuts import render


class IndexView(TemplateView):
    template_name = 'index.html'
    
def acerca_view(request):
    return render(request, 'acerca.html')

def index (request):
    articulos = articulos.objects.all.order_by ('-fecha_publicacion') #agregado a mano para obtener las noticias
    return render (request, 'index.html', {'articulos': articulos})