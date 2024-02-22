from django import forms
from techBlog.models import *
from django.forms import ModelForm, TextInput, Textarea, ClearableFileInput

class BlogForm(forms.ModelForm):
    class Meta:
        model=TechBlog
        fields=['title', 'short_discription', 'content','img']

        widgets = {
            'title': TextInput(attrs={'class': 'input-name  form-control', }),
            'short_discription':TextInput(attrs={'class': 'input-author form-control', }),
            'content':Textarea(attrs={'class': 'input-Discription form-control', }), 
                     
        } 