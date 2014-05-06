from django import forms
from models import Alumno, Curso

class AlumnoForm(forms.ModelForm):
	class Meta:
		model = Alumno
		fields=['rut','nombres','apellidoPaterno','apellidoMaterno','email']


class CursoForm(forms.ModelForm):
	class Meta:
		model = Curso