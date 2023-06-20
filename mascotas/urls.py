from django.urls import path
from .views import Inicio, Tienda, Nosotros, Galeria, Contacto, API, CrearArt, Disponible, Eliminar, Modificar, Registrar, Mostrar

urlpatterns=[ 
    path('', Inicio, name = "Inicio"),
    path('Tienda/', Tienda, name = "Tienda"),
    path('Nosotros/', Nosotros, name = "Nosotros"),
    path('Galeria/', Galeria, name = "Galeria"),
    path('Contacto/', Contacto, name = "Contacto"),
    path('Registrar/', Registrar, name = "Registrar"),
    path('API/', API, name = "API"),
    path('CrearArt/', CrearArt, name = "CrearArt"),
    path('Disponible/', Disponible, name = "Disponible"),
    path('Eliminar/<id>', Eliminar, name = "Eliminar"),
    path('Modificar/<id>', Modificar, name = "Modificar"),
    path('Mostrar/', Mostrar, name = "Mostrar")
] 