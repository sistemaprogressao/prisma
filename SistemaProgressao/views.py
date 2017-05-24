from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect,HttpResponse
from .forms import *

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

#
# o que tenho que fazer funcionar hoje ainda
# cadastrar e login
#

def cadastrar(request):

	if request.method == 'POST':
		formUser = FormUser(request.POST)

		if formUser.is_valid():
			nome = formUser.cleaned_data['first_name']
			sobrenome = formUser.cleaned_data['last_name']
			siape = formUser.cleaned_data['username']
			email = formUser.cleaned_data['email']
			senha = formUser.cleaned_data['password']
			user = User.objects.create_user(siape, email, senha)
			user.first_name = nome
			user.last_name = sobrenome
			user.save()
			Usuario.objects.create(user=user)
			return HttpResponseRedirect(request.POST.get('next'))

	else:
		formUser = FormUser()

	return render(request, 'SistemaProgressao/cadastrar.html', {'formUser': formUser})


def do_login(request):

	if request.method == 'POST':
		u = authenticate(email=request.POST['email'], password=request.POST['password'])

		if u is not None:
			UsuarioLoginForm(request, u)
			return redirect('/main')

	return render(request, 'SistemaProgressao/login.html')

def do_logout(request):
	logout(request)
	return redirect('/apresentacao')

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Senha alterada com sucesso!')
            return redirect('SistemaProgressao:change_password')
        else:
            messages.error(request, 'Senhas incompatíveis.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'SistemaProgressao/change_password.html', {
        'form': form
    })

# teste acima
# cadastrar refutado
# terminar autenticacao hoje
#

@login_required
def main(request):
	return render(request, 'SistemaProgressao/main.html', {})

# historico de atividade do usuario
@login_required
def historico(request):
	form = HistoricoForm()
	return render(request, 'SistemaProgressao/historico.html', {'form': form})

# anexos a serem preenchidos pelos usuarios
@login_required
def documents(request):
	form = DocumentosForm()
	return render(request, 'SistemaProgressao/documents.html',{'form': form})

@login_required
def infogerais(request):
	form = InfoForm()
	return render(request, 'SistemaProgressao/infogerais.html', {'form': form})

def apresentacao(request):
	form = InfoForm()
	return render(request, 'SistemaProgressao/apresentacao.html', {'form': form})

#
# anexos i, ii, iii, iv
#

@login_required
def anexoi(request):
	form = AnexoIForm()
	return render(request, 'SistemaProgressao/anexoi.html', {'form': form})

@login_required
def anexoii(request):
	form = AnexoIIForm()
	return render(request, 'SistemaProgressao/anexoii.html', {'form': form})

@login_required
def anexoiii(request):
	form = AnexoIIIForm()
	return render(request, 'SistemaProgressao/anexoiii.html', {'form': form})

@login_required
def anexoiv(request):
	form = AnexoIVForm()
	return render(request, 'SistemaProgressao/anexoiv.html', {'form': form})

#
# login e cadastro de usuario
#
'''
# cadastrar usuario
def cadastrar(request):

	# dados passados via post
	if request.method == 'POST':
		form = UsuarioLCadastrarForm(request.POST)

		if form.is_valid():
			# se o formulario for valido, salva-lo
			form.save()
			return HttpResponseRedirect('/login/') # redireciona para o login
		else:
			# manter na pagina caso esteja faltando alguma informacao
			return render(request, 'SistemaProgressao/cadastrar.html', {'form': form })

	# se nenhuma informacao for passado, exibir a pagina de cadastro
	return render(request, 'SistemaProgressao/cadastrar.html', {'form': UsuarioLCadastrarForm() })
'''
