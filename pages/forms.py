from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('title', 'image')


class SearchForm(forms.Form):
    ingredient = forms.CharField(max_length=100)
