from django.shortcuts import render

# Create your views here.
def registrar(request):
    return render ( request, 'first_try.html')
def crear_usuario( request ):
    email= request.POST[ 'fristname' ]
    username= request.POST[ 'lastname' ]
    password= request.POST[ 'password' ]
    repeat_password= request.POST[ 'repeat_password' ]
    print (email)
    print (username)
    print (password)

def inicio(request):
    return render ( request, 'inicio_sesion2.html')
def pagina(request):
    return render ( request, 'pagina_inicio2.html')
def cuenta(request):
    return render ( request, 'cuenta.html')
