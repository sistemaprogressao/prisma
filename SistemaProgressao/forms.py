from django import forms
from .models import *

class UsuarioLoginForm(forms.ModelForm):

	senha = forms.CharField(widget=forms.PasswordInput())
	
	# login usuario
	class Meta:
		model = Usuario
		fields = ('siape','senha',)

class UsuarioLCadastrarForm(forms.ModelForm):

	senha = forms.CharField(widget=forms.PasswordInput())

	# cadastro usuario
	class Meta:
		model = Usuario
		fields = ('nome','email','senha','siape',)
		
###
# tudo ok ate aqui
###

class DocumentosForm(forms.ModelForm):
	
	# envio dos documentos
	class Meta:
		model = Documento
		fields = ('link_pdf',)

class HistoricoForm(forms.ModelForm):

	# historico dos formularios do usuario
	class Meta:
		model = Historico
		fields = ('link_pdf_final',)

# informacoes gerais do usuario para preenchimento dos anexos
class InfoForm(forms.ModelForm):
	class Meta:
		model =  InfoGerais
		fields = ('usuario', 'lotacao', 'classe', 'periodo',)

# definicao dos anexos i, ii, iii, iv
class AnexoIForm(forms.ModelForm):

	# anexo i
	class Meta:
		model = AnexoI
		fields = '__all__'

class AnexoIIForm(forms.ModelForm):

	# anexo ii
	class Meta:
		model = AnexoII
		fields = '__all__'

class AnexoIIIForm(forms.ModelForm):

	# anexo iii
	class Meta:
		model = AnexoIII
		fields = '__all__'

class AnexoIVForm(forms.ModelForm):

	# anexo iv
	class Meta:
		model = AnexoIV
		fields = '__all__'

