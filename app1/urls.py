from django.urls import path, include
from . import views 
urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("productos/", views.productos, name="productos"),
    path("acerca_de_mi/", views.acerca_de_mi, name="acerca_de_mi"),
    path("catalogo/", views.catalogo, name="catalogo"),
]
def include_app1_urls():
    return include((urlpatterns, 'app1'), namespace='app1')