from django.contrib.auth.models import User
from django.shortcuts import render
from core.models import Usuario
from core.models import Paciente

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view


from core.models import Colaborador


@api_view(['POST'])
def cadastro_paciente(request):
	if request.method == 'POST':
		usuario = request.data['usuario']
		senha = request.data['senha']
		confirma_senha = request.data['confirmarSenha']
		email = request.data['email']
		nome = request.data['nome']
		telefone = request.data['telefone']
		celular = request.data['celular']
		cpf = request.data['cpf']
		sexo = request.data['sexo']
		orientacao_sexual = request.data['orientacao_sexual']
		paciente = None

		user = User.objects.filter(username=usuario)

		if not user:
			user = User.objects.create_user(usuario, email, senha)
			user.save()

			paciente = Paciente(
				nome=nome,
				telefone_celular=celular,
				telefone_fixo=telefone,
				cpf=cpf,
				email=email,
				sexo=sexo,
				orientacao_sexual=orientacao_sexual
			)

			user = User.objects.get(username=usuario)
			paciente.user = user
			paciente.save()

		response = {
			"status": 200,
			"message": "Paciente cadastrado com sucesso!"
		}

		return Response({"response": response})