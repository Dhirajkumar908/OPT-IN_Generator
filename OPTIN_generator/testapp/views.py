from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView
from .models import *
from .forms import *

# Create your views here.
def home(request):
    return render(request, 'testapp/test.html')

class blog(ListView):
    model=Blog
    template_name='testapp/test.html'
    context_object_name='blogs'

class detail_blog(DetailView):
    model=Blog
    template_name='testapp/detail_post.html'
    context_object_name='blog'

class create_Blog(CreateView):
    model=Blog
    form_class=BlogForm
    template_name='testapp/Create_post.html'
    success_url= reverse_lazy('blog')

class delete_blog(DeleteView):
    model=Blog
    template_name='testapp/test.html' 
    success_url=reverse_lazy('blog')

