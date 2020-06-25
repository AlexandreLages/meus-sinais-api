from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('cadastrar/', views.CadastroColaboradorView.as_view(), name='core_cadastro_colaborador'),
]
