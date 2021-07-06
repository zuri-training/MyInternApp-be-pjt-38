from django.db import models
from django.contrib.auth.models import User

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
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    student_reg_info = models.OneToOneField(StudentRegistration, on_delete=models.CASCADE)
    about = models.TextField(null=True, blank=True)
    course = models.CharField(max_length=100, null=True, blank=True)
    school_id = models.ImageField(blank=True, null=True)
    profile_pic = models.ImageField(blank=True, null=True)
    twitter_handle = models.CharField(max_length=100, blank=True, null=True)
    linkedin_link = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self) -> str:
        return str(self.student_reg_info)

class EmployerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    employer_reg_info = models.OneToOneField(EmployerRegistration, on_delete=models.CASCADE)
    about = models.TextField(null=True, blank=True)
    website = models.CharField(max_length=100, null=True, blank=True)
    rc_number = models.CharField(max_length=100, null=True, blank=True)
    profile_pic = models.ImageField(blank=True, null=True)
    interest = models.CharField(max_length=100, null=True, blank=True)
    twitter_handle = models.CharField(max_length=100, blank=True, null=True)
    linkedin_link = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self) -> str:
        return str(self.employer_reg_info)


class JobPost(models.Model):
    author = models.ForeignKey(EmployerRegistration, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    reference_image = models.ImageField(null=True, blank=True)
    category = models.CharField(max_length=100)
    tags = models.CharField(max_length=100)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    day_posted = models.DateField(auto_now_add=True,blank=True, null=True)
    budget = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

