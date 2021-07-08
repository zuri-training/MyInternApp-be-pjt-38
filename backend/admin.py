from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(EmployerRegistration)
admin.site.register(StudentRegistration)
admin.site.register(StudentProfile)

admin.site.register(JobPost)
admin.site.register(StudentWorkPost)

admin.site.register(EmployerProfile)


