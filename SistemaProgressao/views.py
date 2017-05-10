from django.shortcuts import render
from django.http import HttpResponseRedirect 
from .forms import *

# Main
def main(request):
	return render(request, 'SistemaProgressao/main.html', {})

# historico de atividade do usuario
def historico(request):		
	form = HistoricoForm()
	return render(request, 'SistemaProgressao/historico.html', {'form': form})

# anexos a serem preenchidos pelos usuarios
def documents(request):
	form = DocumentosForm()
	return render(request, 'SistemaProgressao/documents.html',{'form': form})

def infogerais(request):
	form = InfoForm()
	return render(request, 'SistemaProgressao/infogerais.html', {'form': form})

def apresentacao(request):
	form = InfoForm()
	return render(request, 'SistemaProgressao/apresentacao.html', {'form': form})

#
# anexos i, ii, iii, iv
#

def anexoi(request):
	form = AnexoIForm()
	return render(request, 'SistemaProgressao/anexoi.html', {'form': form})

def anexoii(request):
	form = AnexoIIForm()
	return render(request, 'SistemaProgressao/anexoii.html', {'form': form})

def anexoiii(request):
	form = AnexoIIIForm()
	return render(request, 'SistemaProgressao/anexoiii.html', {'form': form})

def anexoiv(request):
	form = AnexoIVForm()
	return render(request, 'SistemaProgressao/anexoiv.html', {'form': form})

#
# login e cadastro de usuario
#

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

# pagina de login
def login(request):
    if request.method == 'POST':
        form = UsuarioLoginForm(data=request.POST) # Veja a documentacao desta funcao
        
        if form.is_valid():
            # se o formulario for valido significa que o Django conseguiu encontrar o usuario no banco de dados
            # agora, basta logar o usuario e ser feliz.
            return HttpResponseRedirect('/main/') # redireciona o usuario logado para a pagina inicial
        else:
            return render(request, 'SistemaProgressao/login.html', {'form': form})
    
    # se nenhuma informacao for passada, exibe a pagina de login com o formulario
    return render(request, 'SistemaProgressao/login.html', {'form': UsuarioLoginForm()})
