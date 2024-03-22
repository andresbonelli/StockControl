from django.shortcuts import render, redirect
# from django.http import HttpResponse, JsonResponse
from .models import Producto, Proveedor
from .forms import ProductoForm, ProveedorForm
# from django.template import Template, Context

def home(request):
    return render(request, 'index.html')

# PRODUCTOS
def listarProductos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})

def crearProducto(request):
    proveedores = Proveedor.objects.all() # pasar el contexto de la DB de proveedores al formulario
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productos_listado')
        else:
            mensaje = "Por favor, complete todos los campos del formulario."
            return render(request, 'crear_producto.html', {'form': form, 'mensaje': mensaje, 'proveedores': proveedores})
    else:
        form = ProductoForm()

    return render(request, 'crear_producto.html', {'form': form, 'proveedores': proveedores})

# PROVEEDORES
def listarProveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'lista_proveedores.html', {'proveedores': proveedores})

def crearProveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('proveedores_listado')
        else:
            mensaje = "Por favor, complete todos los campos del formulario."
            return render(request, 'crear_proveedor.html', {'form': form, 'mensaje': mensaje})

    else:
            form = ProveedorForm()

    return render(request, 'crear_proveedor.html')
