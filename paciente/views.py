from django.contrib.auth.models import User
from core.models import Usuario, Especialidade
from core.models import Paciente

from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def lista_motivos(request):
	especialidades = Especialidade.objects.all()
	lista = []

	for especialidade in especialidades:
		c = {
			'id': especialidade.id,
			'nome': especialidade.nome
		}
		lista.append(c)

	return Response(lista)


@api_view(['POST'])
def cadastro_paciente(request):
	if request.method == 'POST':
		usuario = request.data['usuario']
		senha = request.data['senha']
		email = request.data['email']
		nome = request.data['nome']
		telefone = request.data['telefone']
		celular = request.data['celular']
		cpf = request.data['cpf']
		sexo = request.data['sexo']
		orientacao_sexual = request.data['orientacao_sexual']
		data_nascimento = request.data['data_nascimento']

		user_username = User.objects.filter(username=usuario).first()
		user_cpf = Usuario.objects.filter(cpf=cpf).first()
		user_email = Usuario.objects.filter(email=email).first()

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
		elif user_email is not None:
			response = {
				"status": 409,
				"message": "Já existe um usuário com o mesmo Email!"
			}
			return Response({"response": response})
		else:
			user = User.objects.create_user(usuario, email, senha)
			user.save()

			paciente = Paciente(
				nome=nome,
				telefone_celular=celular,
				telefone_fixo=telefone,
				cpf=cpf,
				email=email,
				sexo=sexo,
				data_nascimento=data_nascimento,
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