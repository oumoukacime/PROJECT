import email
from tkinter import CASCADE
from django.db import models

# Create your models here.
from django.db import models


class Patient(models.Model):
    nom = models.CharField(max_length=35)
    prenom = models.CharField(max_length=35)
    email = models.EmailField(default= "patient@aaaa.aa")
    adresse = models.CharField(max_length=20)

    def __str__(self):
        return self.nom[:35]



class Medecin(models.Model):
    nom = models.CharField(max_length=35)
    prenom = models.CharField(max_length=35)
    email = models.EmailField(default= "medecin@aaaa.aa")
    adresse = models.CharField(max_length=20)
    nom_specialite = models.CharField(max_length= 20)


    def __str__(self):
        return self.prenom[: 35 ]  

class Consultation(models.Model):
    patient = models.ForeignKey(Patient , on_delete=models.CASCADE)
    medecin = models.ForeignKey(Medecin , on_delete=models.CASCADE)
    dateCons= models.DateField(auto_now_add=True)
    description = models.CharField(max_length= 50)
    analyse =models.CharField(default="Consultation sans analyse",max_length=35)


      


