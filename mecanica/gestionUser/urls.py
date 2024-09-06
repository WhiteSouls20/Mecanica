#from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),

    path ('crud_clientes', views.crud_clientes, name='crud_clientes'),
    path ('clientesAdd', views.clientesAdd, name='clientesAdd'),
    path('clientes_del/<str:pk>', views.clientes_del, name='clientes_del'),
    path('clientesUpdate/<str:pk>', views.clientesUpdate, name='clientesUpdate'),
    path('clientesUpdate', views.clientesUpdate, name='clientesUpdate'),

    path('crud_generos', views.crud_generos, name='crud_generos'),
    path('generosAdd', views.generosAdd, name='generosAdd'),
    path('generos_del/<str:pk>', views.generos_del, name='generos_del'),
    path('generos_edit/<str:pk>', views.generos_edit, name='generos_edit'),

    path ('crud_vehiculos', views.crud_vehiculos, name='crud_vehiculos'),
    path ('vehiculosAdd', views.vehiculosAdd, name='vehiculosAdd'),
    path('vehiculos_del/<str:pk>', views.vehiculos_del, name='vehiculos_del'),
    path('vehiculosUpdate/<str:pk>', views.vehiculosUpdate, name='vehiculosUpdate'),
    path('vehiculosUpdate', views.vehiculosUpdate, name='vehiculosUpdate'),            

    path ('estado_vehiculos', views.estado_vehiculos, name='estado_vehiculos'),

    path ('home', views.home, name='home'),    
]