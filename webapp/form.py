from django import forms
from .models import peoples

class NameForm(forms.ModelForm):
    class Meta:
        model = peoples
        fields = '__all__'
