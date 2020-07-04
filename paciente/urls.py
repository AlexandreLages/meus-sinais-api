from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('cadastrar/', views.cadastro_paciente, name='core_cadastro_paciente'),
	path('listar_motivos/', views.lista_motivos, name='core_lista_motivos'),
]
