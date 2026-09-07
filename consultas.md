1. Producto.objects.all()

2. Producto.objects.filter(precio__gt=1000)

3. Producto.objects.filter(precio__lt=5000)

4. Producto.objects.filter(nombre__icontains="mesa")

5. Producto.objects.filter(stock__gt=10)

6. Producto.objects.filter(activo=True)

7. Categoria.objects.create(nombre="Tecnologia",slug="tecnologia")

8. Producto.objects.order_by("-precio")

9. Producto.objects.filter(categoria__nombre__icontains="muebles")

10. categoria = Categoria.objects.get(id=1); categoria.productos.all()
