from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.AutoField(primary_key=True)
    lugar_nacimiento = models.CharField(max_length=150, blank=True)
    fecha_nacimiento = models.DateTimeField(blank=True)
    domicilio = models.CharField(max_length=150, blank=True)
    email = models.EmailField(max_length=70, blank=True)
    sexo = models.BooleanField(null = False)#True = Hombre, False = Madre
    #Datos estandares de persona, estos van a ser heredados x cualquier profesor o alumno

    def genero(self):
        aux = 'Mujer'
        if self.sexo:
            aux = 'Hombre'
            return aux
        else:
            return aux
    '''
    Me crea la variable auxiliar, que por default es mujer, si se marca como true, me devuelve que
    es un hombre, sino, quedara como mujer
    '''

    def __str__(self):
        return 'Persona: {} {}| dni: {}| sexo: {}'.format(self.nombre,
         self.apellido, self.dni, self.genero())

    class Meta:
        abstract = True



class Profesor(Persona):
    #foto = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    telefono_particular_p = models.IntegerField()
    telefono_laboral_p = models.IntegerField()
    telefono_familiar_p = models.IntegerField()
    datos_familiares_cargo = models.TextField(max_length=300)
    fecha_inicio_actividad = models.DateTimeField()
    antecedentes_laborales = models.TextField(max_length=300)
    antiguedad_en_empresa = models.DateTimeField()
    estudios_cursados = models.TextField(max_length=300)

    def __str__(self):
        return 'Persona: {} {}| dni: {}| sexo: {}'.format(self.nombre, self.apellido, self.dni, self.sexo)



class Autorizado(Persona):
    autorizacion = models.BooleanField()

    def __str__(self):
        return 'Persona: {} {}| dni: {}|'.format(self.nombre, self.apellido, self.dni)



class Transportista(Persona):
    nombre_transporte = models.CharField(max_length=40)
    telefono_transportista = models.IntegerField()
    detalles_transportista = models.TextField(max_length=300)

    def __str__(self):
        return 'Persona: {} {}| dni: {}|'.format(self.nombre, self.apellido, self.dni)



class Padre_madre(Persona):
    cant_hijos_en_colegio = models.IntegerField(null=False)
    profesion = models.CharField(max_length=40)
    telefono_trabajo = models.IntegerField()

    def __str__(self):
        return 'Persona: {} {}| dni: {}|'.format(self.nombre, self.apellido, self.dni)



class Alumno(Persona):
    telefono_casa = models.IntegerField()
    telefono_padre = models.IntegerField()
    telefono_madre = models.IntegerField()
    telefono_familiar = models.IntegerField()
    telefono_vecino = models.IntegerField()
    enfermedad_relevante = models.CharField(max_length=40)
    con_quien_vive = models.CharField(max_length=40)
    quien_lo_trae = models.CharField(max_length=40)
    telefono_que_lo_trae = models.IntegerField()
    utiliza_transporte = models.BooleanField() #Si viene o se va en transporte
    transporte = models.ForeignKey(Transportista)
    autorizados = models.ForeignKey(Autorizado)
    padres = models.ForeignKey(Padre_madre)
    tiene_obra_social = models.BooleanField()
    obra_social_nombre = models.CharField(max_length=40, null=True)
    obra_social_numero = models.IntegerField() #Numero de afiliacion a la ora social


    def __str__(self):
        return 'Persona: {} {}| dni: {}| sexo: {}'.format(self.nombre, self.apellido, self.dni, self.sexo)
