from django.shortcuts import render

# Create your views here.
def registrar(request):
    return render ( request, 'first_try.html')
def inicio(request):
    return render ( request, 'inicio_sesion2.html')
def pagina(request):
    return render ( request, 'pagina_inicio2.html')
def cuenta(request):
    return render ( request, 'cuenta.html')
