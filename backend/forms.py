from django.forms import ModelForm
from .models import *

class GeneralRegistrationForm(ModelForm):
	class Meta:
		model = GeneralRegistration
		fields = '__all__'