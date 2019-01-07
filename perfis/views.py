from django.shortcuts import render
from perfis.models import Perfil, Convite
from django.shortcuts import redirect
from django.views.generic.base import View
# Create your views here.

def index(request):
	return render(request, 'index.html',{'perfis' : Perfil.objects.all(),
										 'perfil_logado' : get_perfil_logado(request)})

def exibir_perfil(request, perfil_id):

	perfil = Perfil.objects.get(id=perfil_id)

	return render(request, 'perfil.html',
		          {'perfil' : perfil, 
				   'perfil_logado' : get_perfil_logado(request)})

def convidar(request,perfil_id):

	perfil_a_convidar = Perfil.objects.get(id=perfil_id)
	perfil_logado = get_perfil_logado(request)
	
	if(perfil_logado.pode_convidar(perfil_a_convidar)):
		perfil_logado.convidar(perfil_a_convidar)
	
	return  redirect('index')

def get_perfil_logado(request):
	return Perfil.objects.get(id = 2)

def aceitar(request, convite_id):
	convite = Convite.objects.get(id = convite_id)
	convite.aceitar()
	return redirect('index')

