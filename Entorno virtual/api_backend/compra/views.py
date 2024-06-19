from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,CreateView
from django.middleware.csrf import get_token
from compra.models import Cliente, Producto, Pedido
from compra.serializers import ClienteSerializer, ProductoSerializer, PedidoSerializer
from compra.forms import ClienteForm, ProductoForm, PedidoForm
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect


#View de inicio
def compra(request):
    return render(request, "compra.html")

#Views para listar entidades
def get_all_clientes():
    clientes = Cliente.objects.all().order_by('nombre')
    clientes_serializers = ClienteSerializer(clientes, many=True)
    return clientes_serializers.data

def clientes(request):
    clientes = get_all_clientes()
    return render(request, "clientes.html", {"clientes": clientes})

def get_all_productos():
    productos = Producto.objects.all().order_by('nombre')
    productos_serializers = ProductoSerializer(productos, many=True)
    return productos_serializers.data

def productos(request):
    productos = get_all_productos()
    return render(request, "productos.html", {"productos": productos})

def get_all_pedidos():
    pedidos = Pedido.objects.all().order_by("fecha")
    pedidos_seralizers = PedidoSerializer(pedidos, many=True)
    return pedidos_seralizers.data

def pedidos(request):
    pedidos = get_all_pedidos()
    return render(request, "pedidos.html", {"pedidos": pedidos})

#views para REST API
def clientes_rest(request):
    clientes = get_all_clientes()
    return JsonResponse(clientes, safe=False)

def productos_rest(request):
    productos = get_all_productos()
    return JsonResponse(productos, safe=False)

def pedidos_rest(request):
    pedidos = get_all_pedidos()
    return JsonResponse(pedidos, safe=False)

#View para new entidades
class new_cliente(CreateView):
    form_class = ClienteForm
    template_name = "new_cliente.html" 
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["csrf_token"] = get_token(self.request)
        return context

class new_producto(CreateView):
    form_class = ProductoForm
    template_name = "new_producto.html" 
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["csrf_token"] = get_token(self.request)
        return context

class new_pedido(CreateView):
    form_class = PedidoForm
    template_name = "new_pedido.html" 
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["csrf_token"] = get_token(self.request)
        return context

