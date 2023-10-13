from django import forms
from django.forms import ModelForm
from django.forms import ModelForm, TextInput, Textarea, ClearableFileInput, EmailField
from .models import *

class OptINforms(ModelForm):
    class Meta:
        model=OptIN
        fields=["name","email","number","data","header","footer"]

        # widgets={
        #     'name':forms.TextInput(attrs={'class':'form-control',}),
        #     'email':forms.EmailField(attrs={'class':'form-control'}),
        #     'number':forms.IntegerField(attrs={'class':'form-control'}),
        #     'data':forms.DateField(attrs={'class':'form-control'}),
        #     'header':forms.ImageField(attrs={'class':'form-control'}),
        #     'footer':forms.ImageField(attrs={'class':'form-control'})
        # }


# class contectForm(ModelForm):
#     class Meta:
#         model=contect

#         fields=["name","email","url","comment"]
#         widgets={
#             'name':TextInput(attrs={'class':'C_name', 'style':'width:400px; '  }),
#             'email':TextInput(attrs={'class':'C_name', 'style':'width:400px; '  }),
#             'url':TextInput(attrs={'class':'C_name', 'style':'width:400px; '  }),
#             'comment':TextInput(attrs={'class':'C_name', 'style':'width:400px; height:300px ',  }),
#         }
