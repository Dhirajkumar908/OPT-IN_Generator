from django import forms
from .models import *

class OptINforms(forms.ModelForm):
    class Meta:
        model=OptIN
        fields=['name','email','number','data','header','footer']

        # widgets={
        #     'name':forms.TextInput(attrs={'class':'form-control',}),
        #     'email':forms.EmailField(attrs={'class':'form-control'}),
        #     'number':forms.IntegerField(attrs={'class':'form-control'}),
        #     'data':forms.DateField(attrs={'class':'form-control'}),
        #     'header':forms.ImageField(attrs={'class':'form-control'}),
        #     'footer':forms.ImageField(attrs={'class':'form-control'})
        # }
