from django.db import models

# Create your models here.
class Curso(models.Model):

    nombre=models.CharField(max_length=40)
    camada = models.IntegerField()


class Estudiante(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()

class Profesor(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    profesion= models.CharField(max_length=30)

class Entregable(models.Model):
    nombre= models.CharField(max_length=30)
    fechaDeEntrega = models.DateField()  
    entregado = models.BooleanField()

class Materias(models.Model):
    nombre_materia= models.CharField(max_length=30)
    nombre_profesor_a_cargo= models.CharField(max_length=30)  
    apellido_profesor_a_cargo= models.CharField(max_length=30)
    
class Post_grado(models.Model):
    nombre_grado= models.CharField(max_length=30)
    nombre_profesor_a_cargo= models.CharField(max_length=30)  
    apellido_profesor_a_cargo= models.CharField(max_length=30)
