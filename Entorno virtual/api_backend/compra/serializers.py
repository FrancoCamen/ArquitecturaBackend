from rest_framework import serializers
from compra.models import Cliente, Producto, Pedido

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        # fields = ['name', 'number', 'collection', 'is_backlight']
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        # fields = ['name', 'number', 'collection', 'is_backlight']
        fields = '__all__'