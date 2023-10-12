from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .forms import *
from .models import *
import requests
# Create your views here.

class optinListView(ListView):
    model=OptIN
    template_name='index.html'
    context_object_name='IptIn'


#delete optin
class delete_Optin(DeleteView):
    model=OptIN
    success_url='optinListView'
    