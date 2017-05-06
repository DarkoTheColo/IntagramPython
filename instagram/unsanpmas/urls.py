from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^registrar/$', views.registrar, name = 'registro'),
    url(r'^inicio_sesion/$', views.inicio, name = 'inicio'),
    url(r'^pagina_inicio/$', views.pagina, name = 'pagina'),
    url(r'^cuenta/$', views.cuenta, name = 'cuenta'),
]
