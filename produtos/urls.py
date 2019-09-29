from django.urls import path
from .views import produtos_new
from .views import produtos_list


urlpatterns = [
    path('new/', produtos_new, name="produtos_new"),    
    path('list/', produtos_list, name="produtos_list"),

]