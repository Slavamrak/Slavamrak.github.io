from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.views.generic import DetailView

from .models import *

menu = [1, 2, 3]


def index(request):
    posts = Build.objects.order_by('-pk')[:4]

    context = {
        'posts': posts,
        'title': 'Главная страница',
    }

    return render(request, 'build/index.html', context=context)

def about(request):
		return render(request, 'build/about.html', {'menu': menu, 'title': 'О нас'})

def build(request):
		posts = Build.objects.order_by('-pk')


		context = {
			'posts': posts,
 			'title': 'Ремонт',
		}
		return render(request, 'build/build.html', context=context)

def sale(request):
		sale = Sale.objects.order_by('-pk')


		context = {
			'title': 'Акции',
			'sale': sale, 
		}
		return render(request, 'build/sale.html', context=context)
def feedback(request):
		return render(request, 'build/feedback.html', {'menu': menu, 'title': 'Обратная связь'})

class posts(DetailView):
		model = Build
		template_name = 'build/posts.html'
		context_object_name = 'buil'






def pageNotFound(request, exception):
		return HttpResponseNotFound("<h1> Страница не найдена </h1>")

