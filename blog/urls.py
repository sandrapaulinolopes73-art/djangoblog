from django.urls import path
from . import views
#Rota para anotação de views, que é a função home, que retorna uma resposta HTTP com o texto "Olá, Django!".

urlpatterns = [
    path('', views.home, name='home'),
]