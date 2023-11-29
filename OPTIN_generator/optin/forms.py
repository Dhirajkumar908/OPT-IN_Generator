from django import forms
from django.forms import DateInput, NumberInput, DateTimeInput

from .models import *

class OptINforms(forms.ModelForm):
    # data = forms.DateField(widget=forms.SelectDateWidget)
    
    class Meta:
        model=OptIN
        fields=["name","email","number","data","HeaderFooter"]
        widgets = {
            'data':  DateTimeInput( format=('%D-%M-%Y'),attrs={'type': 'date' }),
            'number':NumberInput(attrs={'type':'number'})       
               }

       
