from django.conf.urls import include,url
from . import views

# definindo a chamada da view, o arquivo HTML
urlpatterns = [
	url(r'^$', views.apresentacao),
	url(r'^cadastrar/$', views.cadastrar),
	url(r'^login/$', views.login),	
	url(r'^documents/$', views.documents),
	url(r'^infogerais/$', views.infogerais),
	url(r'^main/', views.main),
	url(r'^historico/$', views.historico),
	url(r'^anexoi/$', views.anexoi),
	url(r'^anexoii/$', views.anexoii),
	url(r'^anexoiii/$', views.anexoiii),
	url(r'^anexoiv/$', views.anexoiv),	
	url(r'^apresentacao/$', views.apresentacao),
]

# funcionandooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo