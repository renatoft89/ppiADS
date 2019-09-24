from django.urls import path
from .views import empresas_new
from .views import empresas_update
from .views import empresas_delete

urlpatterns = [
    path('new/', empresas_new, name="empresas_new"),
    path('update/<int:id>', empresas_update, name="empresas_update"),
    path('delete/<int:id>', empresas_delete, name="empresas_delete"),

]