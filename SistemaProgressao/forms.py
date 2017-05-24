from django import forms
from .models import *
from django.forms import ModelForm, TextInput

class FormUser(forms.ModelForm):

	first_name = forms.CharField(label='Nome', max_length=30)
	last_name = forms.CharField(label='Sobrenome', max_length=30)
	email = forms.EmailField(label='Email')

	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'username', 'email', 'password']
		widget = {
			'username': TextInput(attrs={'id':'id-username'}),
			'password': TextInput(attrs={'id':'id-password', 'type':'password'}),
		}
		labels = {
			'username': ('SIAPE:'),
			'password': ('Senha:'),
		}
		help_texts = {
			'username': '',
		}
'''
class UsuarioLoginForm(forms.ModelForm):

	password = forms.CharField(widget=forms.PasswordInput())

	# login usuario
	class Meta:
		model = Usuario
		fields = ('email','password',)
		widget = {
			'email': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 254}),
			'password': forms.PasswordInput(attrs={'class': 'form-control', 'maxlength': 254}),
		}

	def save(self, commit=True):
		usuario = super(UsuarioModelForm, self).save(commit=False)
		usuario.set_password(self.cleaned_data['password'])

		if commit:
			usuario.save()

		return usuario
'''
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
