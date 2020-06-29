from django.contrib.auth.models import User
from django.shortcuts import render
from core.models import Usuario

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view


from core.models import Colaborador


@api_view(['POST'])
def cadastro_colaborador(request):
	if request.method == 'POST':
		usuario = request.data['usuario']
		senha = request.data['senha']
		email = request.data['email']
		nome = request.data['nome']
		telefone = request.data['telefone']
		celular = request.data['celular']
		cpf = request.data['cpf']
		rg = request.data['rg']
		crp = request.data['crp']
		perfil = request.data['perfil']

		user_username = User.objects.filter(username=usuario).first()
		user_cpf = Usuario.objects.filter(cpf=cpf).first()
		colaborador_email = Colaborador.objects.filter(email=email).first()
		colaborador_crp = Colaborador.objects.filter(crp=crp).first()

		if user_username is not None:
			response = {
				"status": 409,
				"message": "Já existe um usuário com o mesmo Usuário!"
			}
			return Response({"response": response})
		elif user_cpf is not None:
			response = {
				"status": 409,
				"message": "Já existe um usuário com o mesmo CPF!"
			}
			return Response({"response": response})
		elif colaborador_email is not None:
			response = {
				"status": 409,
				"message": "Já existe um usuário com o mesmo Email!"
			}
			return Response({"response": response})
		elif colaborador_crp is not None:
			response = {
				"status": 409,
				"message": "Já existe um usuário com o mesmo CRP!"
			}
			return Response({"response": response})
		else:
			user = User.objects.create_user(usuario, email, senha)
			user.save()

			colaborador = Colaborador(
				nome=nome,
				telefone_celular=celular,
				telefone_fixo=telefone,
				cpf=cpf,
				rg=rg, email=email,
				crp=crp, perfil=perfil
			)
			user = User.objects.get(username=usuario)
			colaborador.user = user
			colaborador.save()
			response = {
				"status": 200,
				"message": "Usuário cadastrado com sucesso!"
			}
			return Response({"response": response})



@api_view(['GET'])
def lista_colaborador(request):
	if request.method == 'GET':
		colaboradores = Colaborador.objects.all()
		lista = []

		for colaborador in colaboradores:
			c = {
				'usuario': colaborador.user.username,
				'nome': colaborador.nome,
				'telefone_celular': colaborador.telefone_celular,
				'telefone_fixo': colaborador.telefone_fixo,
				'cpf': colaborador.cpf,
				'rg': colaborador.rg,
				'email': colaborador.email,
				'sexo': colaborador.sexo,
				'crp': colaborador.crp,
				'perfil': colaborador.perfil
			}

			lista.append(c)

		return Response(lista)
