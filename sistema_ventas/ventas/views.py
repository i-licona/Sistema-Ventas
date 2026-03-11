from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.db import models
from .application.services import ClienteService, ProductoService, VentaService, CategoriaService, ProveedorService
from .forms import CategoriaForm, ProductoForm, ClienteForm, ProveedorForm, VentaForm, DetalleVentaForm
from .infrastructure.django_models import CategoriaModel, ProductoModel, ClienteModel, ProveedorModel, VentaModel, DetalleVentaModel

cliente_service = ClienteService()
producto_service = ProductoService()
venta_service = VentaService()
categoria_service = CategoriaService()
proveedor_service = ProveedorService()

# ==================== VISTAS INICIALES ====================
def inicio(request):
    total_clientes = len(cliente_service.get_all_clientes())
    total_productos = len(producto_service.get_all_productos())
    total_ventas = len(venta_service.get_all_ventas())
    total_categorias = len(categoria_service.get_all_categorias())
    total_proveedores = len(proveedor_service.get_all_proveedores())

    context = {
        'total_clientes': total_clientes,
        'total_productos': total_productos,
        'total_ventas': total_ventas,
        'total_categorias': total_categorias,
        'total_proveedores': total_proveedores,
    }
    return render(request, 'ventas/index.html', context)


# ==================== CRUD CATEGORÍAS ====================
def lista_categorias(request):
    categorias = categoria_service.get_all_categorias()
    return render(request, 'ventas/categorias/lista.html', {'categorias': categorias})


@require_http_methods(["GET", "POST"])
def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            categoria_model = form.save()
            categoria_service.create_categoria(categoria_model)
            return redirect('lista_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'ventas/categorias/formulario.html', {'form': form, 'titulo': 'Crear Categoría'})


@require_http_methods(["GET", "POST"])
def editar_categoria(request, categoria_id):
    categoria_model = get_object_or_404(CategoriaModel, id=categoria_id)
    
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria_model)
        if form.is_valid():
            categoria_model = form.save()
            categoria_service.update_categoria(categoria_id, categoria_model)
            return redirect('lista_categorias')
    else:
        form = CategoriaForm(instance=categoria_model)
    
    return render(request, 'ventas/categorias/formulario.html', {'form': form, 'titulo': 'Editar Categoría', 'id': categoria_id})


@require_http_methods(["GET", "POST", "DELETE"])
def eliminar_categoria(request, categoria_id):
    if request.method == 'DELETE' or (request.method == 'POST' and request.POST.get('confirmar') == 'si'):
        categoria_service.delete_categoria(categoria_id)
        if request.method == 'DELETE':
            return JsonResponse({'mensaje': 'Categoría eliminada'})
        return redirect('lista_categorias')
    
    categoria = categoria_service.get_categoria_by_id(categoria_id)
    return render(request, 'ventas/categorias/confirmar_delete.html', {'categoria': categoria})


# ==================== CRUD PRODUCTOS ====================
def lista_productos(request):
    productos = producto_service.get_all_productos()
    return render(request, 'ventas/productos/lista.html', {'productos': productos})


@require_http_methods(["GET", "POST"])
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto_model = form.save()
            producto_service.create_producto(producto_model)
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'ventas/productos/formulario.html', {'form': form, 'titulo': 'Crear Producto'})


@require_http_methods(["GET", "POST"])
def editar_producto(request, producto_id):
    producto_model = get_object_or_404(ProductoModel, id=producto_id)
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto_model)
        if form.is_valid():
            producto_model = form.save()
            producto_service.update_producto(producto_id, producto_model)
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto_model)
    
    return render(request, 'ventas/productos/formulario.html', {'form': form, 'titulo': 'Editar Producto', 'id': producto_id})


@require_http_methods(["GET", "POST", "DELETE"])
def eliminar_producto(request, producto_id):
    if request.method == 'DELETE' or (request.method == 'POST' and request.POST.get('confirmar') == 'si'):
        producto_service.delete_producto(producto_id)
        if request.method == 'DELETE':
            return JsonResponse({'mensaje': 'Producto eliminado'})
        return redirect('lista_productos')
    
    producto = producto_service.get_producto_by_id(producto_id)
    return render(request, 'ventas/productos/confirmar_delete.html', {'producto': producto})


# ==================== CRUD CLIENTES ====================
def lista_clientes(request):
    clientes = cliente_service.get_all_clientes()
    return render(request, 'ventas/clientes/lista.html', {'clientes': clientes})


@require_http_methods(["GET", "POST"])
def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente_model = form.save()
            cliente_service.create_cliente(cliente_model)
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'ventas/clientes/formulario.html', {'form': form, 'titulo': 'Crear Cliente'})


@require_http_methods(["GET", "POST"])
def editar_cliente(request, cliente_id):
    cliente_model = get_object_or_404(ClienteModel, id=cliente_id)
    
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente_model)
        if form.is_valid():
            cliente_model = form.save()
            cliente_service.update_cliente(cliente_id, cliente_model)
            return redirect('lista_clientes')
    else:
        form = ClienteForm(instance=cliente_model)
    
    return render(request, 'ventas/clientes/formulario.html', {'form': form, 'titulo': 'Editar Cliente', 'id': cliente_id})


@require_http_methods(["GET", "POST", "DELETE"])
def eliminar_cliente(request, cliente_id):
    if request.method == 'DELETE' or (request.method == 'POST' and request.POST.get('confirmar') == 'si'):
        cliente_service.delete_cliente(cliente_id)
        if request.method == 'DELETE':
            return JsonResponse({'mensaje': 'Cliente eliminado'})
        return redirect('lista_clientes')
    
    cliente = cliente_service.get_cliente_by_id(cliente_id)
    return render(request, 'ventas/clientes/confirmar_delete.html', {'cliente': cliente})


# ==================== CRUD PROVEEDORES ====================
def lista_proveedores(request):
    proveedores = proveedor_service.get_all_proveedores()
    return render(request, 'ventas/proveedores/lista.html', {'proveedores': proveedores})


@require_http_methods(["GET", "POST"])
def crear_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            proveedor_model = form.save()
            proveedor_service.create_proveedor(proveedor_model)
            return redirect('lista_proveedores')
    else:
        form = ProveedorForm()
    return render(request, 'ventas/proveedores/formulario.html', {'form': form, 'titulo': 'Crear Proveedor'})


@require_http_methods(["GET", "POST"])
def editar_proveedor(request, proveedor_id):
    proveedor_model = get_object_or_404(ProveedorModel, id=proveedor_id)
    
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor_model)
        if form.is_valid():
            proveedor_model = form.save()
            proveedor_service.update_proveedor(proveedor_id, proveedor_model)
            return redirect('lista_proveedores')
    else:
        form = ProveedorForm(instance=proveedor_model)
    
    return render(request, 'ventas/proveedores/formulario.html', {'form': form, 'titulo': 'Editar Proveedor', 'id': proveedor_id})


@require_http_methods(["GET", "POST", "DELETE"])
def eliminar_proveedor(request, proveedor_id):
    if request.method == 'DELETE' or (request.method == 'POST' and request.POST.get('confirmar') == 'si'):
        proveedor_service.delete_proveedor(proveedor_id)
        if request.method == 'DELETE':
            return JsonResponse({'mensaje': 'Proveedor eliminado'})
        return redirect('lista_proveedores')
    
    proveedor = proveedor_service.get_proveedor_by_id(proveedor_id)
    return render(request, 'ventas/proveedores/confirmar_delete.html', {'proveedor': proveedor})


# ==================== VISTAS VENTAS ====================
def lista_ventas(request):
    ventas = venta_service.get_all_ventas()
    ventas.sort(key=lambda v: v.fecha, reverse=True)
    return render(request, 'ventas/ventas/lista.html', {'ventas': ventas})


@require_http_methods(["GET", "POST"])
def crear_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            venta_model = form.save(commit=False)
            venta_model.save()
            return redirect('editar_venta', venta_id=venta_model.id)
    else:
        form = VentaForm()
    
    productos = ProductoModel.objects.filter(stock__gt=0)
    return render(request, 'ventas/ventas/crear.html', {'form': form, 'productos': productos})


@require_http_methods(["GET", "POST"])
def editar_venta(request, venta_id):
    venta_model = get_object_or_404(VentaModel, id=venta_id)
    venta = venta_service.get_venta_by_id(venta_id)
    
    if request.method == 'POST':
        # Si viene del formulario, solo guardamos, no actualizamos el cliente
        return redirect('editar_venta', venta_id=venta_id)
    
    productos = ProductoModel.objects.filter(stock__gt=0)
    detalles = DetalleVentaModel.objects.filter(venta=venta_model)
    
    return render(request, 'ventas/ventas/editar.html', {
        'form': None,
        'venta': venta,
        'detalles': detalles,
        'productos': productos,
        'venta_id': venta_id
    })


@require_http_methods(["POST"])
def agregar_producto_venta(request, venta_id):
    """Agregar producto a una venta (AJAX)"""
    try:
        import json
        venta_model = get_object_or_404(VentaModel, id=venta_id)
        
        # Manejar tanto JSON como POST form data
        if request.content_type == 'application/json':
            data = json.loads(request.body)
            producto_id = data.get('producto_id')
            cantidad = int(data.get('cantidad', 1))
        else:
            producto_id = request.POST.get('producto_id')
            cantidad = int(request.POST.get('cantidad', 1))
        
        producto_model = get_object_or_404(ProductoModel, id=producto_id)
        
        if cantidad <= 0:
            return JsonResponse({'error': 'Cantidad debe ser mayor a 0'}, status=400)
        
        if cantidad > producto_model.stock:
            return JsonResponse({'error': f'Stock insuficiente. Disponible: {producto_model.stock}'}, status=400)
        
        # Verificar si el producto ya existe en la venta
        detalle = DetalleVentaModel.objects.filter(venta=venta_model, producto=producto_model).first()
        
        if detalle:
            # Actualizar cantidad
            nueva_cantidad = detalle.cantidad + cantidad
            if nueva_cantidad > producto_model.stock + detalle.cantidad:
                return JsonResponse({'error': f'Stock insuficiente. Disponible: {producto_model.stock}'}, status=400)
            detalle.cantidad = nueva_cantidad
            detalle.subtotal = detalle.precio_unitario * nueva_cantidad
            detalle.save()
        else:
            # Crear nuevo detalle
            precio_unitario = float(producto_model.precio)
            subtotal = precio_unitario * cantidad
            DetalleVentaModel.objects.create(
                venta=venta_model,
                producto=producto_model,
                cantidad=cantidad,
                precio_unitario=precio_unitario,
                subtotal=subtotal
            )
        
        # Actualizar total
        total = DetalleVentaModel.objects.filter(venta=venta_model).aggregate(models.Sum('subtotal'))['subtotal__sum'] or 0
        venta_model.total = total
        venta_model.save()
        
        return JsonResponse({'success': True, 'total': float(venta_model.total)})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@require_http_methods(["POST"])
def eliminar_detalle_venta(request, detalle_id):
    """Eliminar producto de una venta"""
    try:
        detalle = get_object_or_404(DetalleVentaModel, id=detalle_id)
        venta_id = detalle.venta.id
        venta_service.eliminar_detalle_venta(detalle_id)
        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@require_http_methods(["POST"])
def guardar_venta(request, venta_id):
    """Guardar venta y descontar stock"""
    try:
        venta_model = get_object_or_404(VentaModel, id=venta_id)
        detalles = DetalleVentaModel.objects.filter(venta=venta_model)
        
        if not detalles.exists():
            return JsonResponse({'error': 'La venta debe tener al menos un producto'}, status=400)
        
        # Descontar stock de todos los productos
        for detalle in detalles:
            producto_service.actualizar_stock(detalle.producto.id, detalle.cantidad)
        
        # Actualizar total
        total = detalles.aggregate(models.Sum('subtotal'))['subtotal__sum'] or 0
        venta_model.total = total
        venta_model.save()
        
        return redirect('detalle_venta', venta_id=venta_id)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def detalle_venta(request, venta_id):
    """Ver detalles de una venta"""
    venta = venta_service.get_venta_by_id(venta_id)
    detalles = DetalleVentaModel.objects.filter(venta_id=venta_id)
    
    return render(request, 'ventas/ventas/detalle.html', {
        'venta': venta,
        'detalles': detalles
    })


@require_http_methods(["GET", "POST", "DELETE"])
def eliminar_venta(request, venta_id):
    """Eliminar una venta"""
    if request.method == 'DELETE' or (request.method == 'POST' and request.POST.get('confirmar') == 'si'):
        venta_service.delete_venta(venta_id)
        if request.method == 'DELETE':
            return JsonResponse({'mensaje': 'Venta eliminada'})
        return redirect('lista_ventas')
    
    venta = venta_service.get_venta_by_id(venta_id)
    detalles = DetalleVentaModel.objects.filter(venta_id=venta_id)
    return render(request, 'ventas/ventas/confirmar_delete.html', {
        'venta': venta,
        'detalles': detalles
    })