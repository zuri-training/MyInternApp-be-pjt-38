from django.contrib import admin
from .models import EmployerRegistration, StudentRegistration, GeneralRegistration


# Register your models here.
admin.site.register(EmployerRegistration)
admin.site.register(StudentRegistration)
admin.site.register(GeneralRegistration)