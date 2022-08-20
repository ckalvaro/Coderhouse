from django.urls import path
from FamiliApp.views import familiapp_inicio
urlpatterns = [
    path('', familiapp_inicio, name='familiapp_inicio'),
    
]
