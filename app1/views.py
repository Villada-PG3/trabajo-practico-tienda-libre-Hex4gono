from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto
# Create your views here.
def productos(request):
    lista_productos = Producto.objects.all()

    contexto = {
        "productos": lista_productos
    }

    return render(request, "app1/productos.html", contexto)

def hello_world(request):
    return render(request, "app1/hello_world.html")

def home(request):
    productos = [
        {'nombre': 'Auriculares Sony WH-1000XM5', 'marca': 'Sony', 'descripcion': 'Cancelación de ruido y hasta 30 horas de batería.', 'precio': 349.99, 'stock': 8},
        {'nombre': 'iPhone 15', 'marca': 'Apple', 'descripcion': 'Pantalla Super Retina XDR y cámara principal de 48 MP.', 'precio': 799.00, 'stock': 0},
        {'nombre': 'Notebook Galaxy Book4', 'marca': 'Samsung', 'descripcion': 'Laptop liviana con procesador Intel Core y pantalla Full HD.', 'precio': 949.99, 'stock': 4},
        {'nombre': 'Nintendo Switch OLED', 'marca': 'Nintendo', 'descripcion': 'Consola híbrida con pantalla OLED de 7 pulgadas.', 'precio': 349.99, 'stock': 0},
        {'nombre': 'Cafetera Nespresso Essenza Mini', 'marca': 'Nespresso', 'descripcion': 'Café espresso en cápsulas con diseño compacto.', 'precio': 129.90, 'stock': 12},
        {'nombre': 'Zapatillas Air Max 270', 'marca': 'Nike', 'descripcion': 'Amortiguación visible y comodidad para todos los días.', 'precio': None, 'stock': 3},
    ]

    context = {
        "productos": productos
    }
    return render(request, "app1/home.html", {"productos": productos})

def acerca_de_mi(request):
    return render(request, "app1/acerca_de_mi.html")