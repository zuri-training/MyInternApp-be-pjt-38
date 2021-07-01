from django.db import models

# Create your models here.

class StudentRegistration(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200, unique=True)
    phone = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=250)
    school = models.CharField(max_length=250)
    level = models.CharField(max_length=250)
    skills = models.TextField()


    def __str__(self):
        return self.first_name + ' - ' + self.email 



class EmployerRegistration(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200, unique=True)
    phone = models.CharField(max_length=100)
    country = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    business_name = models.CharField(max_length=250)
    gender = models.CharField(max_length=10)
    role = models.CharField(max_length=250)
    address = models.TextField()
    

    def __str__(self):
        return self.business_name + ' ' + self.email