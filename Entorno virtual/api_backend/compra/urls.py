from django.urls import path
from compra import views

urlpatterns = [
    path('', views.compra, name='compra'),

    path('clientes/', views.clientes, name='clientes'),
    path('productos/', views.productos, name='productos'),
    path('pedidos/', views.pedidos, name='pedidos'),

    path('clientes_rest/', views.clientes_rest, name='clientes_rest'),
    path('productos_rest/', views.productos_rest, name='productos_rest'),
    path('pedidos_rest/', views.pedidos_rest, name='pedidos_rest'),

    path('new_cliente/', views.new_cliente.as_view(), name='new_cliente'),
    path('new_producto/', views.new_producto.as_view(), name='new_producto'),
    path('new_pedido/', views.new_pedido.as_view(), name='new_pedido'),
]
