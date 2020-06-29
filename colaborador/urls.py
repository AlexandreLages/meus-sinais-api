from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('cadastrar/', views.cadastro_colaborador, name='core_cadastro_colaborador'),
	path('listar/', views.lista_colaborador, name='core_lista_colaborador'),
]
