from django.db import models

# Create your models here.

class Doctor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    specialty = models.OneToOneField(Specialty)
    years_of_experience = models.IntegerField()
    patients = models.ManyToOneRel(Patient) 




class Specialty(models.Model):
    name = models.CharField(max_length=20)