from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

class CadastroColaboradorView(APIView):

	def post(self, request):
		usuario = request.data['usuario']
		senha = request.data['senha']
		confirma_senha = request.data['confirmarSenha']
		email = request.data['email']
		nome = request.data['nome']
		telefone = request.data['telefone']
		celular = request.data['celular']
		cpf = request.data['cpf']
		rg = request.data['rg']
		crp = request.data['crp']
		perfil = request.data['perfil']

		user = User.objects.filter(username=usuario)

		if not user:
			user = User.objects.create_user(usuario, email, senha)
			user.save()

			colaborador = Colaborador(
				nome=nome,
				telefone_celular=celular,
				telefone_fixo=telefone,
				cpf=cpf,
				rg=rg, email=email,
				crp=crp, perfil=perfil,
				foto=foto
			)

			user = User.objects.get(username=usuario)
			colaborador.user = user
			colaborador.save()
		else:
			response = {
				"status": 409,
				"message": "Já existe um usuário com dados conflitantes!" 
			}
			return Response({"response": response})

		response = {
			"status": 200,
			"message": "Usuário cadastrado com sucesso!" 
		}

		return Response({"response": responses})