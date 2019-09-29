from django.urls import path
from .views import anuncios_new
from .views import anuncios_list


urlpatterns = [
    path('new/', anuncios_new, name="anuncios_new"),    
    path('list/', anuncios_list, name="anuncios_list"),

]