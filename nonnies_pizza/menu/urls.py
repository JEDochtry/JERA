from django.urls import path
from . import views
'''
urlpatterns = [path("menu/", views.menu, name = "menu"),

]
'''
urlpatterns = [
    
    path('menu/', views.menu, name='menu'),
    
]