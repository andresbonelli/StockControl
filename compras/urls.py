from django.urls import path
from . import views

urlpatterns = [
    path('compras', views.home, name="home"),

    path('compras/productos', views.listarProductos, name="productos_listado"),
    path('compras/productos/listado', views.listarProductos, name="productos_listado"),
    path('compras/productos/crear', views.crearProducto, name="productos_crear"),

    path('compras/proveedores', views.listarProveedores, name="proveedores_listado"),
    path('compras/proveedores/listado', views.listarProveedores, name="proveedores_listado"),
    path('compras/proveedores/crear', views.crearProveedor, name="proveedores_crear"),

]