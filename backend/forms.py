from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import *

class GeneralRegistrationForm(ModelForm):
	class Meta:
		model = GeneralRegistration
		fields = '__all__'

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
        fields = ['username', 'email', 'password1', 'password2']