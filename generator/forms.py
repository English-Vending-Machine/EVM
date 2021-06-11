from django import forms
from .models import problem

class ImageForm(forms.ModelForm):
    class Meta:
        model = problem
        fields = ('image',)