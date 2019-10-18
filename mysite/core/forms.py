from django import forms
from .models import PontoTuristico

class PontoTuristicoForm(forms.ModelForm):
	class Meta:
		model = PontoTuristico
		fields = ('idPonto','nome', 'categoria', 'latitude', 'longitude')