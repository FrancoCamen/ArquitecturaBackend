from django import forms

from compra.models import Cliente, Producto, Pedido

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["dni","nombre","direccion","correo"]

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ["id","nombre","descripcion","total"]

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ["id","fecha","cantidad","total","cliente","productos"]
