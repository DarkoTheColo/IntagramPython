from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^registrar/$', views.registrar, name = 'registro'),
    url(r'^crear_usuario/$', views.crear_usuario, name = 'crear_usuario'),
    url(r'^pagina_inicio/$', views.pagina, name = 'pagina'),
    url(r'^cuenta/$', views.cuenta, name = 'cuenta'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='inicio_sesion2.html', redirect_authenticated_user=True), name= 'login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name= 'first_try.html'), name = 'logout'),
]
