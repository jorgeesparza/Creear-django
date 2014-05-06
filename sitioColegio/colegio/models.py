#import Librerias
import datetime
from django.utils 				import timezone
from django.db 					import models
from django.contrib.auth.models import User
from django.db.models.signals 	import post_save
from django.core.exceptions 	import ValidationError
from django.conf 				import settings



#funciones globales
def usernamePresentes(username):
    if User.objects.filter(username=username).count():
        return True
    return False

def emailPresente(email):
    if User.objects.filter(email=email).count():
        return True
    return False

# Create your models here.
#alumno
class Alumno (models.Model):
	rut 			= models.CharField('Rut', 				max_length=20, unique=True, )#validators=[validaRut])
	nombres 		= models.CharField('Nombres', 			max_length=200)
	apellidoPaterno = models.CharField('Apellido Paterno', 	max_length=100)
	apellidoMaterno = models.CharField('Apelliedo Materno', 	max_length=100)
	email 			= models.EmailField(					max_length=200, unique=True)
	avatar 			= models.ImageField(					upload_to='images/%Y/%m/%d',	null=True)
	activo          = models.BooleanField(					default=True)
	#foraneas
	user 			= models.OneToOneField(User)
	curso			= models.ForeignKey('Curso',			verbose_name="Curso", null = True)


	def __unicode__(self):
		return self.nombres

	def CambioPassword(self,password):
		self.user.set_password(password)
		if self.user.save():
			return True
		return True

	def AsignarCurso(self,id_curso):
		curso = Curso.objects.filter(id=id)
		self.curso = curso
		self.save()



	def Editar(self, data):
		if data:
			print data
			alumno = self
			user = User.objects.get(id = alumno.user.id)
			alumno.rut = data['rut']
			alumno.nombres=data['nombres']
			alumno.apellidoPaterno = data['app']
			alumno.email = data['email']
			alumno.apellidoMaterno = data['apm']
			#alumno.curso=data['curso']

			if data['avatar'] != 0:
				alumno.avatar = data['avatar']
				print 'model.avatar'

			alumno.save()
			return alumno.id
		else:
			return 0

	@staticmethod
	def crear(data):
		retorno = {}
		retorno['codigo'] = 0
		retorno['descripcion'] = ''
		if data:
			if usernamePresentes(data['rut']):
				print 'rut duplicado'
				retorno['codigo'] = 601
				retorno['descripcion'] = 'Rut Ya Existente en nuestro sistema'
				return retorno
			elif emailPresente(data['email']):
				print 'Email duplicado'
				retorno['codigo'] = 602
				retorno['descripcion'] = 'El Email Ya Existente en nuestro sistema'
				return retorno
			else:
				user = User.objects.create_user(username = data['rut'],password = data['password'],email=data['email'],first_name=data['nombres'],last_name = data['app'])
				alumno = Alumno(rut = data['rut'],nombres=data['nombres'],apellidoPaterno = data['app'],email = data['email'],apellidoMaterno = data['apm'], user = user)
				
				if data['avatar']:
					alumno.avatar = data['avatar']

				alumno.save()
				retorno['codigo'] = 600
				retorno['descripcion'] = 'Se ha creado correctamente'
				return retorno
		return retorno;

	
	@staticmethod
	def All():
		return Alumno.objects.all()

	@staticmethod
	def ListaOrdenRut():
		return Alumno.objects.order_by('rut')

	@staticmethod
	def BuscarId(id):
		return Alumno.objects.get(id=id)






#Curso
class Curso(models.Model):
	nombre 		= models.CharField('Nombre',			max_length=50)
	ano			= models.CharField('Ano',				max_length=4)
	nivel		= models.IntegerField('Nivel',			max_length=3)

	def __unicode__(self):
		return self.nombre

	def editar(self,nombre,ano,nivel):
		self.nombre = nombre
		self.ano = ano
		self.nivel = nivel
		self.save()
		return self

	def asignarAlumnos(self,data):
		if data:
			for i in xrange(1,len(data)):
				alumno = Alumno.objects.filter(id=data[i])
				alumno.curso = self
				alumno.save()
		return True

	@staticmethod
	def crear(nombre,ano,nivel):
		cursoCreado = Curso.objects.create(nombre = nombre, ano = ano, nivel = nivel)
		return cursoCreado











