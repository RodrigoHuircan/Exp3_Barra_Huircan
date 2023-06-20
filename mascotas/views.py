from django.shortcuts import render, redirect
from .models import Articulo
from .forms import ArticuloForm, RegistroUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

# Create your views here.

def Inicio(request):
    return render(request,'Inicio.html')

def Tienda(request):
    return render(request,'Tienda.html')

def Nosotros(request):
    return render(request,'Nosotros.html')

def Galeria(request):
    return render(request,'Galeria.html')

def Contacto(request):
    return render(request,'Contacto.html')

def API(request):
    return render(request,'API.html')


@login_required
def Disponible(request):
    articulos = Articulo.objects.raw('SELECT * FROM mascotas_articulo')
    print(articulos)
    datos = {'articulos' : articulos}
    return render(request, 'Disponible.html', datos)


@login_required
def CrearArt(request):
    if request.method == "POST":
        articuloform = ArticuloForm(request.POST,request.FILES) 
        if articuloform.is_valid():
            articuloform.save() 
            return redirect ('Disponible')
    else:
        articuloform=ArticuloForm()
    return render(request, 'CrearArt.html', {'articuloform' : ArticuloForm})

@login_required
def Eliminar(request, id):
    articuloEliminado=Articulo.objects.get(codigo=id) 
    articuloEliminado.delete()
    return redirect('Disponible')


@login_required
def Modificar(request, id):
    articuloModificado = Articulo.objects.get(codigo=id)
    datos ={
        'form': ArticuloForm(instance=articuloModificado) 
    }
    if request.method=="POST":
        formulario = ArticuloForm(data=request.POST, instance=articuloModificado)
        if formulario.is_valid():
            formulario.save()
            return redirect('Disponible')
    return render(request,'Modificar.html', datos)

def Registrar(request):
    data={
        'form':RegistroUserForm()
    }
    if request.method=="POST":
        formulario=RegistroUserForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user=authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request,user)
            return redirect ('Inicio')
        data["form"]=formulario   
    return render(request,'registration/Registrar.html', data)

def Mostrar(request):
    articulitos = Articulo.objects.all()
    datos = {
        'articulitos': articulitos
    }
    return render(request, 'Mostrar.html', datos)

