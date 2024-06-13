from django.urls import path, re_path

from .views import *

urlpatterns = [
		path('', index, name='home'),
		path('about/', about, name='about'),
		path('build/', build, name='build'),
		path('feedback/', feedback, name='feedback'),
		path('posts/<int:pk>/', posts.as_view(), name='posts'),
		path('sale', sale, name='sale')
]
