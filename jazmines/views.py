

from django.shortcuts import render
from django.shortcuts import render_to_response





# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def gallery(request):
    return render(request, 'gallery.html')

def planes(request):
    return render(request, 'planes.html')

def contact(request):
    return render(request, 'contact.html')


def construccion(request):
    return render(request, 'construccion.html')

def obituarios(request):
    return render(request, 'obituarios.html')

def terminos(request):
    return render(request, 'terminos.html')

def alianzas(request):
    return render(request, 'alianzas.html')



def contacto_empresa(request):
    return render(request, 'contacto_empresa.html')


def login(request):
        return render(request, 'login.html')


def sesion_obituarios(request):
    return render(request, 'sesion_obituarios.html')

def sesion_usuario(request):
    return render(request, 'sesion_usuario.html')

def sesion_eventos(request):
    return render(request, 'sesion_eventos.html')

def actualizar_noticias(request):
    return render(request, 'actualizar_noticias.html')

def agregar_obituarios(request):
    return render(request, 'agregar_obituarios.html')

def agregar_eventos(request):
    return render(request, 'agregar_eventos.html')

def historico_eventos(request):
    return render(request, 'historico_eventos.html')

def historico_obituarios(request):
    return render(request, 'historico_obituarios.html')

def modificar_eventos(request):
    return render(request, 'modificar_eventos.html')

def modificar_obituarios(request):
    return render(request, 'modificar_obituarios.html')

def agregar_usuario(request):
    return render(request, 'agregar_usuario.html')


def modificar_usuario(request):
    return render(request, 'modificar_usuario.html')

def visualizar_usuarios(request):
    return render(request, 'visualizar_usuario.html')




              




