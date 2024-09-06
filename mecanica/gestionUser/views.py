from django.shortcuts import render
from .models import Cliente, Genero, Vehiculo

from .forms import GeneroForm
from .forms import ClienteForm
from .forms import VehiculoForm

from django.contrib.auth.decorators import login_required

# Create your views here.

# def index (request):
#     clientes = Cliente.objects.all()
#     context = {"clientes":clientes}
#     return render (request, 'gestionUser/index.html', context)


def crud_clientes (request):
    clientes = Cliente.objects.all()
    context = {'clientes':clientes}
    return render (request, 'gestionUser/clientes_list.html', context)

def clientesAdd(request):

    context={}
    if request.method == "POST":
        form=ClienteForm(request.POST)
        if form.is_valid:
           form.save()

           #limpiar form
           form=ClienteForm()

           context={'mensaje':'datos grabados',"form":form}
           return render(request,'gestionUser/clientes_add.html',context)
    
    else:
        form=ClienteForm()
        context={'form':form}
        return render(request,'gestionUser/clientes_add.html',context)    

def clientes_del (request, pk):
    context={}
    try:
        cliente=Cliente.objects.get(rut=pk)

        cliente.delete()
        mensaje="Bien, datos eliminados..."
        clientes = Cliente.objects.all()
        context = {'clientes': clientes, 'mensaje': mensaje}
        return render(request, 'gestionUser/clientes_list.html', context)
    except:
        mensaje="Error, rut no existe..."
        clientes=Cliente.objects.all()
        context = {'clientes': clientes, 'mensaje': mensaje}
        return render(request, 'gestionUser/clientes_list.html', context)
    
def clientes_findEdit(request, pk):

    if pk !="":
        cliente=Cliente.objects.get(rut=pk)
        generos=Genero.objects.all()

        print(type(cliente.id_genero.genero))

        context={'cliente':cliente, 'generos':generos}
        if cliente:
            return render(request, 'gestionUser/clientes_edit.html', context)
        else:
            context={'mensaje':"Error, rut no existe..."}
            return render (request, 'gestionUser/clientes_list.html', context)    
        
def clientesUpdate (request, pk):
    try:
        cliente=Cliente.objects.get(rut=pk)
        context={}
        if cliente:
            print("Edit encontro el genero...")
            if request.method =="POST":
                print("edit, es un post")
                form= ClienteForm (request.POST, instance=cliente)
                form.save()
                mensaje="Bien, datos actualizados..."
                print(mensaje)
                context = {'cliente':cliente, 'form':form, 'mensaje':mensaje}
                return render (request, 'gestionUser/clientes_edit.html', context)
            else:
                #No es un post
                print("edit, NO es un POST")
                form= ClienteForm(instance=cliente)
                mensaje=""
                context = {'cliente':cliente, 'form':form, 'mensaje':mensaje}
                return render (request, 'gestionUser/clientes_edit.html', context)
    except:
        print("Error, id no existe...")
        clientes=Cliente.objects.all()
        mensaje="Error, id no existe"
        context={'mensaje':mensaje, 'clientes':clientes}
        return render (request, 'gestionUser/clientes_list.html', context)   

def crud_generos(request):
    generos=Genero.objects.all()
    context={'generos':generos}
    print("enviando datos generos_list")
    return render(request,"gestionUser/generos_list.html", context)

def generosAdd(request):
    print("estoy en controlador generosAdd...")
    context={}

    if request.method == "POST":
        print("controlador es un post...")
        form = GeneroForm(request.POST)
        if form.is_valid:
            print("estoy en agregar, is_valid")
            form.save()


            #limpiar form

            form = GeneroForm()

            context={'mensaje':"Ok, datos grabados...", "form":form}
            return render(request, 'gestionUser/generos_add.html', context)

    else:
        form= GeneroForm()
        context={'form':form}
        return render(request, 'gestionUser/generos_add.html', context)
        
def generos_del (request, pk):
    mensajes=[]
    errores=[]
    generos = Genero.objects.all()
    try:
        genero=Genero.objects.get(id_genero=pk)
        context={}
        if genero:
            genero.delete()
            mensajes.append("Bien, datos eliminados...")
            context={'generos':generos, 'mensajes':mensajes, 'errores': errores}
            return render (request, "gestionUser/generos_list.html", context)
    except:
        print("Error, id no existe...")
        generos=Genero.objects.all()
        mensaje="Error, id no existe"
        context={'mensaje':mensaje, 'generos':generos}
        return render (request, "gestionUser/generos_list.html", context)

def generos_edit (request, pk):
    try:
        genero=Genero.objects.get(id_genero=pk)
        context={}
        if genero:
            print("Edit encontgro el genero...")
            if request.method =="POST":
                print("ewdtir, es un POST")
                form= GeneroForm(request.POST, instance=genero)
                form.save()
                mensaje="Bien, datos actualizados..."
                print(mensaje)
                context = {'genero':genero, 'form':form,'mensaje':mensaje}
                return render (request, 'gestionUser/generos_edit.html', context)
            else:
                #no es un POST
                print("!edit, NO es un POST")
                form = GeneroForm(instance=genero)
                mensaje=""
                context = {'genero':genero, 'form':form, 'mensaje':mensaje}
                return render (request, 'gestionUser/generos_edit.html', context)
    except:
        print("Error, id no existe...")
        generos=Genero.objects.all()
        mensaje="Error, id no existe"
        context={'mensaje':mensaje, 'generos':generos}
        return render (request, 'gestionUser/generos_list.html', context)         
    
def crud_vehiculos (request):
    vehiculos = Vehiculo.objects.all()
    context = {'vehiculos':vehiculos}
    return render (request, 'gestionUser/vehiculos_list.html', context)

def vehiculosAdd(request):

    context={}
    if request.method == "POST":
        form=VehiculoForm(request.POST)
        if form.is_valid:
           form.save()

           #limpiar form
           form=VehiculoForm()

           context={'mensaje':'datos grabados',"form":form}
           return render(request,'gestionUser/vehiculos_add.html',context)
    
    else:
        form=VehiculoForm()
        context={'form':form}
        return render(request,'gestionUser/vehiculos_add.html',context)    

def vehiculos_del (request, pk):
    context={}
    try:
        vehiculo=Vehiculo.objects.get(id_patente=pk)

        vehiculo.delete()
        mensaje="Bien, datos eliminados..."
        vehiculos = Vehiculo.objects.all()
        context = {'vehiculos': vehiculos, 'mensaje': mensaje}
        return render(request, 'gestionUser/vehiculos_list.html', context)
    except:
        mensaje="Error, rut no existe..."
        vehiculos=Vehiculo.objects.all()
        context = {'vehiculos': vehiculos, 'mensaje': mensaje}
        return render(request, 'gestionUser/vehiculos_list.html', context)
    
def vehiculos_findEdit(request, pk):

    if pk !="":
        vehiculo=Vehiculo.objects.get(id_patente=pk)
        clientes=Cliente.objects.get(rut=pk)

        print(type(vehiculo.rut.rut))

        context={'vehiculo':vehiculo, 'clientes':clientes}
        if vehiculo:
            return render(request, 'gestionUser/vehiculos_edit.html', context)
        else:
            context={'mensaje':"Error, rut no existe..."}
            return render (request, 'gestionUser/vehiculos_list.html', context)    
        
def vehiculosUpdate (request, pk):
    try:
        vehiculo=Vehiculo.objects.get(id_patente=pk)
        context={}
        if vehiculo:
            print("Edit encontro el genero...")
            if request.method =="POST":
                print("edit, es un post")
                form= VehiculoForm (request.POST, instance=vehiculo)
                form.save()
                mensaje="Bien, datos actualizados..."
                print(mensaje)
                context = {'vehiculo':vehiculo, 'form':form, 'mensaje':mensaje}
                return render (request, 'gestionUser/vehiculos_edit.html', context)
            else:
                #No es un post
                print("edit, NO es un POST")
                form= VehiculoForm(instance=vehiculo)
                mensaje=""
                context = {'vehiculo':vehiculo, 'form':form, 'mensaje':mensaje}
                return render (request, 'gestionUser/vehiculos_edit.html', context)
    except:
        print("Error, id no existe...")
        vehiculos=Vehiculo.objects.all()
        mensaje="Error, id no existe"
        context={'mensaje':mensaje, 'vehiculos':vehiculos}
        return render (request, 'gestionUser/vehiculos_list.html', context)
    

def estado_vehiculos (request):
    vehiculos = Vehiculo.objects.all()
    context = {'vehiculos':vehiculos}
    return render (request, 'gestionUser/vehiculos_estado.html', context) 

def home (request):
    context= {}
    return render (request, 'gestionUser/home.html')


@login_required
def index(request):
    request.session["usuario"] = "mati"  # Aquí debes usar "usuario" en minúscula
    usuario = request.session["usuario"]
    context = {'usuario': usuario}
    return render(request, 'gestionUser/index.html', context)
