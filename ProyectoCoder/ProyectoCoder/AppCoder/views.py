from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import *

# Create your views here.

def curso(request):

      curso =  Curso(nombre="Desarrollo web", camada="19881")
      curso.save()
      documentoDeTexto = f"--->Curso: {curso.nombre}   Camada: {curso.camada}"


      return HttpResponse(documentoDeTexto)


def inicio(request):

      return render(request, "AppCoder/inicio.html")



def estudiantes(request):

      return render(request, "AppCoder/estudiantes.html")


def entregables(request):

      return render(request, "AppCoder/entregables.html")


def cursos(request):

      if request.method == 'POST':

            miFormulario = CursoFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  curso = Curso (nombre=informacion['curso'], camada=informacion['camada']) 

                  curso.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= CursoFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/cursos.html", {"miFormulario":miFormulario})




def profesores(request):

      if request.method == 'POST':

            miFormulario = ProfesorFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  profesor = Profesor (nombre=informacion['nombre'], apellido=informacion['apellido'],
                   email=informacion['email'], profesion=informacion['profesion']) 

                  profesor.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= ProfesorFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/profesores.html", {"miFormulario":miFormulario})






def buscar(request):

      if  request.GET["camada"]:

	      #respuesta = f"Estoy buscando la camada nro: {request.GET['camada'] }" 
            camada = request.GET['camada'] 
            cursos = Curso.objects.filter(camada__icontains=camada)

            return render(request, "AppCoder/inicio.html", {"cursos":cursos, "camada":camada})

      else: 

	      respuesta = "No enviaste datos"

      
      return HttpResponse(respuesta)

def buscarmateria(request):

      if  request.GET["materia"]:
            
            materia = request.GET['materia'] 
            materias = Materias.objects.filter(nombre_materia__icontains=materia)

            return render(request, "AppCoder/inicio.html", {"materias":materias,
                              "materia":materia})

      else: 

	      respuesta = "No enviaste datos"

      
      return HttpResponse(respuesta)

def buscarpost_grados(request):

      if  request.GET["grado"]:
            
            grado = request.GET['grado'] 
            grados = Post_grado.objects.filter(nombre_grado__icontains=grado)

            return render(request, "AppCoder/inicio.html", {"grados":grados,
                              "grado":grado})

      else: 

	      respuesta = "No enviaste datos"

      
      return HttpResponse(respuesta)

def materias(request):

      if request.method == 'POST':

            miFormulario = MateriaFormulario(request.POST)

            print(miFormulario)

            if miFormulario.is_valid:

                  informacion = miFormulario.cleaned_data

                  materia = Materias (nombre_materia=informacion['nombre_materia'],
                   nombre_profesor_a_cargo=informacion['nombre_profesor_a_cargo'],
                   apellido_profesor_a_cargo=informacion['apellido_profesor_a_cargo'])
                   

                  materia.save()

                  return render(request, "AppCoder/inicio.html")

      else: 

            miFormulario= MateriaFormulario()

      return render(request, "AppCoder/materias.html", {"miFormulario":miFormulario})


def grados(request):
      if request.method == 'POST':
            miFormulario = PostGradoFormulario(request.POST)
            print(miFormulario)
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  post_grados = Post_grado (nombre_grado=informacion['nombre_grado'],
                   nombre_profesor_a_cargo=informacion['nombre_profesor_a_cargo'],
                   apellido_profesor_a_cargo=informacion['apellido_profesor_a_cargo'])
                  post_grados.save()
                  return render(request, "AppCoder/inicio.html")
      else: 
            miFormulario= PostGradoFormulario()

      return render(request, "AppCoder/postgrados.html", {"miFormulario":miFormulario})


def estudiantes(request):
      if request.method == 'POST':
            miFormulario = EstudiantesFormulario(request.POST)
            print(miFormulario)
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  estudiante= Estudiante (nombre=informacion['nombre_estudiante'],
                   apellido=informacion['apellido_estudiante'])
                  estudiante.save()
                  return render(request, "AppCoder/inicio.html")
      else: 
            miFormulario= EstudiantesFormulario()
      return render(request, "AppCoder/estudiantes.html", {"miFormulario":miFormulario})

def buscar_estudiantes(request):

      if  request.GET["estudiante"]:
            
            estudiante = request.GET['estudiante'] 
            estudiantes = Estudiante.objects.filter(nombre__icontains=estudiante)

            return render(request, "AppCoder/inicio.html", {"estudiantes":estudiantes,
                              "estudiante":estudiante})

      else: 

	      respuesta = "No enviaste datos"

      
      return HttpResponse(respuesta)
