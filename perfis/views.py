from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from perfis.models import Perfil, Convite
from django.shortcuts import redirect
from django.views.generic.base import View
# Create your views here.

from django.contrib.auth import logout
def perfil_logado(request):
    return Perfil.objects.get(usuario=request.user)

@login_required
def index(request):
    perfil=perfil_logado(request)



    return render(request, 'index.html',{'perfis' : Perfil.objects.all(),
										 'perfil_logado' : perfil})



def exibir_perfil(request, perfil_id):

	perfil = Perfil.objects.get(id=perfil_id)

	return render(request, 'perfil.html',
		          {'perfil' : perfil, 
				   'perfil_logado' : perfil_logado(request)})

def convidar(request,perfil_id):

	perfil_a_convidar = Perfil.objects.get(id=perfil_id)
	perfil=perfil_logado(request)
	
	#if(perfil_logado.pode_convidar(perfil_a_convidar)):
	perfil.convidar(perfil_a_convidar)
	
	return  redirect('index')


def aceitar(request, convite_id):
	convite = Convite.objects.get(id = convite_id)
	convite.aceitar()
	return redirect('index')

def recusar(request, convite_id):
	convite = Convite.objects.get(id = convite_id)
	convite.recusar()
	return redirect('index')
