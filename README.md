# [Alkemy](https://education.alkemy.org/) - Curso POO en Python
## TP Final Integrador: Sistema de Gestión de Personas.

Consiste de una aplicación CRUD ("Crear, Leer, Actualizar, Borrar") sencilla, desarrollada sobre Django y Python.
Permite al usuario manejar un listado de productos y proveedores (inventario) desde una interfase web.
La app permite la funcionalidad de añadir, modificar y borrar asi como generar un listado de productos y proveedores en una base de datos relacional SQL,
tanto desde el front-end como el panel de administrador.
La flexibilidad de Django y la organización modular del proyecto permite una fácil modificacion del código fuente para eventualmente
ampliar los campos de la base de datos y la futura implementacion de nuevas vistas, creación de nuevos modelos y refactorización de los existentes. 

## Características

- **Vistas de Producto**: Agregar, ver, editar, y eliminar productos.
- **Vistas de Provedor**: Agregar, ver, editar, y eliminar proveedores.
- **Interfase de usuario**: Navegación simple e intuitiva desde browser.
- **Manejo de datos**: INtegración de Django Forms para validación de formularios desde el input de usuario.

## Principal Tecnología usada

- **Django**: Framework web de aplicaciones web en lenguaje Python.
- **Python**: Lenguaje de alto nivel sobre el cual se desarrollo el backend.
- **Jinja**: Motor de manejo de variables y pasaje de datos para el renderizado de plantillas HTML con sintaxis Python.
- **HTML/CSS**: Lenguaje de marcado y estilos para renderizado de interfaz de usuario.
- **Bootstrap**: Framework de diseño responsivo de UI.
- **SQLite**: Sistema de almacenamiento de datos integrado con Django.

## Instalación

- Bajar repositorio al sistema local:
```bash
git clone https://github.com/andresbonelli/StockControl.git
```
- Instalar las dependencias necesarias:
```bash
pip install -r requirements.txt
```
- Iniciar el servidor Django en modo desarrollo:
```bash
python manage.py runserver
```
  

