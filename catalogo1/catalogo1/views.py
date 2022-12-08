from django.shortcuts import render
from productos.models import productos
template_name = "index.html"

"""p = productos.objects.create(
nombre ="pantalo",
precio= 2000,
descripcion = "vintage","""""

productos = productos.objects.all()
contexto = {
    'productos': productos
}
def inicio(requets):
    return render(requets, template_name,contexto)

