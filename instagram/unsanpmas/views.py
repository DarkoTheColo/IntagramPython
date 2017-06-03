from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from unsanpmas.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def registrar(request):
    return render ( request, 'first_try.html')

def crear_usuario( request ):
    _email= request.POST[ 'email' ]
    _username= request.POST[ 'username' ]
    _password= request.POST[ 'password' ]
    _repeat_password= request.POST[ 'repeat_password' ]

    if _password==_repeat_password:
        print (_email)
        print (_username)
        print (_password)
        print (_repeat_password)
        user=User.objects.create_user ( username=_username, email=_email,
        password=_password)
        myUser = MiUsuario ( usuario = user )
        myUser.save()
        print (user)
        print (user.password)
        return redirect( 'login' )
    else:
        return render( request,'login' )


@login_required
def pagina(request):
    return render ( request, 'pagina_inicio2.html')


def cuenta(request):
    user = request.user
    return render ( request, 'cuenta.html', { 'user' : user })
