from django.db import models #cada model funciona como uma tabela, cada atributo seria uma coluna

class User(models.Model):
    email = models.EmailField(max_length = 50)
    password = models.CharField(max_length = 15)

class Place(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 100)
    latitude = models.DecimalField(max_digits = 10, decimal_places = 6)
    longitude = models.DecimalField(max_digits = 10, decimal_places = 6)

