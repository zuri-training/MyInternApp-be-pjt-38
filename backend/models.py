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
        return self.first_name + ' - ' + self.email  + ' student'



class EmployerRegistration(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    email = models.EmailField(max_length=200, unique=True)
    phone = models.CharField(max_length=100)
    country = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    business_name = models.CharField(max_length=250)
    role = models.CharField(max_length=250)
    address = models.TextField()
    

    def __str__(self):
        return self.business_name + ' ' + self.email + ' employer'

class StudentProfile(models.Model):
    student_reg_info = models.OneToOneField(StudentRegistration, on_delete=models.CASCADE)
    about = models.TextField(null=True, blank=True)
    course = models.CharField(max_length=100, null=True, blank=True)
    school_id = models.ImageField(blank=True, null=True)
    profile_pic = models.ImageField(blank=True, null=True)
    twitter_handle = models.CharField(max_length=100)
    linkedin_link = models.CharField(max_length=500)

    def __str__(self) -> str:
        return str(self.student_reg_info)

