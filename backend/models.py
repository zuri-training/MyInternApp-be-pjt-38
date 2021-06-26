from django.db import models
from django.core.validators import RegexValidator


# Create your models here.

class StudentRegistration(models.Model):

    GENDER_CHOICE =(
        ('M', 'Male'), ('F', 'Female'), ('O', 'Others'),
    )

    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    occupation = models.CharField(max_length=250)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE)
    email = models.EmailField(max_length=200)
    phoneRegex = RegexValidator(regex=r"^\+?\d{8,15}$")
    phone = models.CharField(validators=[phoneRegex], max_length=16, unique=True)
    country = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    school = models.CharField(max_length=250)
    levelRegex = RegexValidator(r'^[0-9a-zA-Z]')
    level = models.CharField(max_length=20, validators=[levelRegex])
    interest = models.CharField(max_length=250)


    def __str__(self):
        return (self.first_name)


class EmployerRegistration(models.Model):

    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    occupation = models.CharField(max_length=250)
    gender = models.CharField(max_length=1, choices=StudentRegistration.GENDER_CHOICE)
    email = models.EmailField(max_length=250)
    phone = models.CharField(validators=[StudentRegistration.phoneRegex], max_length=16, unique=True)
    country = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    business_name = models.CharField(max_length=250)
    role = models.CharField(max_length=250)
    address = models.TextField()
    

    def __str__(self):
        return self.business_name