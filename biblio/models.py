# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
# Modelos para guardar informacion referida a los libros
class Autores(models.Model):
	ID = models.AutoField(null=False,unique=True,primary_key=True)
	Nombres = models.CharField(max_length=100,null=False)
	ApellidoMaterno = models.CharField(max_length=100,null=False)
	ApellidoPaterno = models.CharField(max_length=100,null=False)
	PaisNacimiento = models.CharField(max_length=100,null=False)
	FechaNacimiento = models.DateField(null=False)
	class Meta:
		db_table="Autores"

class Editoriales(models.Model):
	ID = models.AutoField(null=False,unique=True,primary_key=True)
	Nombre = models.CharField(max_length=100,null=False)
	Estado = models.CharField(max_length=100,null=False)
	Pais = models.CharField(max_length=50,null=False)
	class Meta:
		db_table="Editoriales"	

class Libros(models.Model):
	ID = models.CharField(max_length=10,null=False,unique=True,primary_key=True)
	Nombre = models.CharField(max_length=100,null=False)
	Autores = models.ManyToManyField(Autores)
	Year = models.IntegerField(verbose_name="Año")
	Edicion = models.IntegerField()
	Editorial = models.ForeignKey(Editoriales)
	Paginas = models.IntegerField()
	ISBN = models.CharField(max_length=17,null=False)
	Ejemplares = models.IntegerField()
	class Meta:
		db_table="Libros"

class Sinopsis(models.Model):
	Libro = models.ForeignKey(Libros)
	Descripcion = models.TextField()
	class Meta:
		db_table="Sinopsis"	

#Modelos para guardar informacion referida a los prestamos y los lectores.
class Lectores(models.Model):
	ID = models.AutoField(null=False,unique=True,primary_key=True)
	Nombre = models.CharField(max_length=200,null=False)
	FechaNacimiento = models.DateField(null=False)
	Direccion = models.CharField(max_length=100,null=False)
	Telefono = models.CharField(max_length=18,null=False)
	Email = models.EmailField(blank=True)
	class Meta:
		db_table="Lectores"	

class Prestamos(models.Model):
	Libros = models.ManyToManyField(Libros)
	Lector = models.ForeignKey(Lectores)
	FechaPrestamo = models.DateTimeField(auto_now=True)
	class Meta:
		db_table="Prestamos"	

class Devoluciones(models.Model):
	Libro = models.ForeignKey(Libros)
	FechaPrestamo = models.DateTimeField(auto_now=True)
	class Meta:
		db_table="Devoluciones"	

class Multas(models.Model):
	Libro = models.ForeignKey(Libros)
	Prestamo = models.ForeignKey(Prestamos)
	Importe = models.DecimalField(null=False,max_digits=5, decimal_places=2)
	class Meta:
		db_table="Multas"