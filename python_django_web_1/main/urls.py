from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('add', views.add, name='add'),
    path('sign_up', views.sign_up, name='sign_up')
]
