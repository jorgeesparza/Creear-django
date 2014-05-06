from django.conf.urls import patterns, url, include

from colegio import views


urlpatterns = patterns('',
	url(r'^$', views.index,name ='index'),
	url(r'^crear_alumno/', views.crearAlumno, name='crear_alumno'),
	url(r'^crear_curso/', views.crearCurso, name='crear_curso'),
	url(r'^alumno_curso/', views.alumnoCurso, name='alumno_curso'),
	url(r'^editar_alumno/', views.editarAlumno, name='editar_alumno'),
)
