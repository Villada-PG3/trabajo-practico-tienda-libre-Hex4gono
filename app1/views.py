from django.views.generic import DetailView, ListView, TemplateView
from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from .models import Categoria, Producto
# Create your views here.
def productos(request):
    lista_productos = Producto.objects.all()

    contexto = {
        "productos": lista_productos
    }

    return render(request, "app1/productos.html", contexto)

def hello_world(request):
    return render(request, "app1/hello_world.html")

class HomeView(TemplateView):
    template_name = "app1/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["productos"] = Producto.objects.order_by("-fecha_creacion")[:3]
        return context

def acerca_de_mi(request):
    return render(request, "app1/acerca_de_mi.html")

class CatalogoView(ListView):
    model = Producto
    template_name = "app1/catalogo.html"
    context_object_name = "productos"
    ordering = "-fecha_creacion"
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        termino = self.request.GET.get("q", "").strip()
        if termino:
            queryset = queryset.filter(
                Q(nombre__icontains=termino)
                | Q(marca__icontains=termino)
                | Q(descripcion__icontains=termino)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["termino_busqueda"] = self.request.GET.get("q", "")
        context["page_range"] = context["paginator"].get_elided_page_range(
            context["page_obj"].number
        )
        return context


class CategoriaView(ListView):
    model = Producto
    template_name = "app1/categoria.html"
    context_object_name = "productos"
    ordering = "-fecha_creacion"
    paginate_by = 6

    def get_queryset(self):
        self.categoria = get_object_or_404(Categoria, slug=self.kwargs["slug"])
        return super().get_queryset().filter(categoria=self.categoria)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categoria"] = self.categoria
        context["page_range"] = context["paginator"].get_elided_page_range(
            context["page_obj"].number
        )
        return context


class DetalleProductoView(DetailView):
    model = Producto
    template_name = "app1/detalle.html"
    context_object_name = "producto"