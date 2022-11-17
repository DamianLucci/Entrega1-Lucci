from django.urls import path
from AppCoder import views





urlpatterns = [
   
    path('', views.inicio, name="Inicio"),
    path('cursos', views.cursos, name="Cursos"),
    path('profesores', views.profesores, name="Profesores"),
    path('estudiantes', views.estudiantes, name="Estudiantes"),
    path('entregables', views.entregables, name="Entregables"),
    path('materias', views.materias, name="Materias"),
    path('postgrados', views.grados, name="postgrados"),
    path('buscar/', views.buscar),
    path('buscarmateria/', views.buscarmateria),
    path('buscarpost_grados/', views.buscarpost_grados),
    path('buscar_estudiantes/', views.buscar_estudiantes),
   
]

