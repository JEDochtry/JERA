from django.urls import path
from . import views

urlpatterns = [
    path('menu2/', views.menu2, name='menu2'),
    path('menu2/details/<int:id>', views.details, name='details'),
    #path('', views.main, name='main'),
    path('', views.landing, name='landing'),
    path('menu2/menu', views.menu, name='menu'),
]