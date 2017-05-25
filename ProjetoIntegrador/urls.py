from django.conf.urls import url, include
from django.contrib import admin

# construtor geral das minhas urls
urlpatterns = [
	# por padrao um administrador
	# adionado chamada para a url do Sistema
    url(r'^admin/', admin.site.urls),
    url(r'', include('SistemaProgressao.urls', namespace='SistemaProgressao', app_name='SistemaProgressao')),
]
