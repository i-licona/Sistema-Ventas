from django.shortcuts import render
from .models import Cliente, Producto, Venta

def inicio(request):
    total_clientes = Cliente.objects.count()
    total_productos = Producto.objects.count()
    total_ventas = Venta.objects.count()

    return render(request, 'ventas/index.html', context)


def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'ventas/clientes/lista.html', {'clientes': clientes})


def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'ventas/productos/lista.html', {'productos': productos})


def lista_ventas(request):
    ventas = Venta.objects.all().order_by('-fecha')
    return render(request, 'ventas/ventas/lista.html', {'ventas': ventas})