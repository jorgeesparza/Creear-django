from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader, Context,RequestContext

from django.shortcuts import render_to_response

from forms import *
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from colegio.models import Alumno, Curso


def index(request):
    template = loader.get_template('index.html')
    
    latest_alumnos_list = Alumno.ListaOrdenRut()
    print latest_alumnos_list
    context = RequestContext(request, { 'latest_alumnos_list': latest_alumnos_list,})
    return HttpResponse(template.render(context))

def crearAlumno(request):
    if request.POST:
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            return HttpResponseRedirect('/colegio/')
    else:
        form = AlumnoForm()
    
    args = {}
    args.update(csrf(request))
    
    args['form'] = form
 
    return render_to_response('crear_alumno.html', args)

def crearCurso(request):
    if request.POST:
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/colegio/')
    else:
        form = CursoForm()
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render_to_response('crear_curso.html', args)


def alumnoCurso(request):

    template = loader.get_template('alumnos_curso.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

def editarAlumno(request):
    if request.POST:
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
 
            return HttpResponseRedirect('/colegio/')
    else:

        form = AlumnoForm()
    args = {}
    args.update(csrf(request))
    print request
    args['form'] = form
 
    return render_to_response('crear_alumno.html', args)

def editarCurso(request):
    if request.POST:
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/colegio/')
    else:
        form = CursoForm()
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render_to_response('crear_curso.html', args)