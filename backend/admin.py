from django.contrib import admin
from .models import EmployerRegistration, StudentRegistration


# Register your models here.
admin.site.register(EmployerRegistration)
admin.site.register(StudentRegistration)