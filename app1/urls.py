from django.urls import path, include
from . import views 
urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("home/", views.HomeView.as_view(), name="home"),
    path("productos/", views.productos, name="productos"),
    path("acerca_de_mi/", views.acerca_de_mi, name="acerca_de_mi"),
    path("catalogo/", views.CatalogoView.as_view(), name="catalogo"),
    path("categoria/<slug:slug>/", views.CategoriaView.as_view(), name="categoria"),
    path('producto/<int:pk>/', views.DetalleProductoView.as_view(), name='detalle_producto'),
]
def include_app1_urls():
    return include((urlpatterns, 'app1'), namespace='app1')