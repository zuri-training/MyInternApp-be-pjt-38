from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import *



class StudentRegistrationForm(ModelForm):
	class Meta:
		model = StudentRegistration
		fields = '__all__'

class EmployerRegistrationForm(ModelForm):
	class Meta:
		model = EmployerRegistration
		fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class StudentProfileForm(ModelForm):
	class Meta:
		model = StudentProfile
		fields = ('student_reg_info',)

class StudentProfileUpdateForm(ModelForm):
	class Meta:
		model = StudentProfile
		fields = '__all__'
		exclude = ['user','student_reg_info']