
from django.db import models

class AdminLogin(models.Model):
    USERNAME=models.CharField(max_length=30,unique=True)
    PASSWORD=models.CharField(max_length=30)


class Disease(models.Model):
    DISEASE_NAME=models.CharField(max_length=30)
    SYMPTOMS=models.CharField(max_length=30)

class Medicine(models.Model):
    DISEASE_NAME = models.CharField(max_length=30)
    SYMPTOMS = models.CharField(max_length=30)
    MEDICINE_NAME=models.CharField(max_length=30)
    MEDICINE_DESCRIPTION=models.CharField(max_length=30)


