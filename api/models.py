from django.db import models #cada model funciona como uma tabela, cada atributo seria uma coluna

class User(models.Model):
    email = models.EmailField(max_length = 50)
    password = models.CharField(max_length = 15)

class Place(models.Model):
    id = models.AutoField(primary_key = True, auto_created=True)
    name = models.CharField(max_length = 100)
    latitude = models.DecimalField(max_digits = 10, decimal_places = 6)
    longitude = models.DecimalField(max_digits = 10, decimal_places = 6)

