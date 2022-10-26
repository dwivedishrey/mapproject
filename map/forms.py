from django import forms
from .models import Search
class SearchForm(forms.ModelForm):
    #address=forms.CharField(label='')
    destination=forms.CharField(label='')
    class Meta:
        model=Search
        fields=['destination', ]
