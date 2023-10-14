from django import forms
from .models import *

class OptINforms(forms.ModelForm):
    class Meta:
        model=OptIN
        fields=["name","email","number","data","header","footer"]

        # def __init__(self, *args, **kwargs):
        #     super(OptINforms, self) 