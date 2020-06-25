from django.shortcuts import render

# Libs - Requisição
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view


class BemVindoView(APIView):

	def get(self, request):
		return Response({"response": "Bem-Vindo(a) ao Meus Sinais!"})