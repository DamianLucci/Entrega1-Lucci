from django import forms


class CursoFormulario(forms.Form):

    #Especificar los campos
    curso = forms.CharField()
    camada = forms.IntegerField()


class ProfesorFormulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    profesion= forms.CharField(max_length=30)
    
class MateriaFormulario(forms.Form):   
    nombre_materia= forms.CharField(max_length=30)
    nombre_profesor_a_cargo= forms.CharField(max_length=30)  
    apellido_profesor_a_cargo= forms.CharField(max_length=30)

class PostGradoFormulario(forms.Form):
    nombre_grado= forms.CharField(max_length=30)
    nombre_profesor_a_cargo= forms.CharField(max_length=30)  
    apellido_profesor_a_cargo= forms.CharField(max_length=30)  
 
 

class EstudiantesFormulario(forms.Form):
    nombre_estudiante= forms.CharField(max_length=30)
    apellido_estudiante= forms.CharField(max_length=30)  
 