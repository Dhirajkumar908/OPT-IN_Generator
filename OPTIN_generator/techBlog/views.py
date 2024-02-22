from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from techBlog.models import *
from techBlog.forms import *
from django.contrib.auth.decorators import user_passes_test
from optin.views import is_user_authenticated
# Create your views here.

class posts_list_views(ListView):
    model=TechBlog
    template_name='blog/blogs.html'
    context_object_name='blogs'

def detail_view(request, pk):
    post=TechBlog.objects.get(pk=pk)
    return render(request, 'blog/techblog.html', {'post':post})


# class create_post(CreateView):
#     models=TechBlog
#     form_class=BlogForm
#     template_name='blog/post_create_from.html'
#     succcess_url=reverse_lazy('posts_list_views')
@user_passes_test(is_user_authenticated, login_url='userlogin')
def create_post(request):
    if request.method=="POST":
        form_data=BlogForm(request.POST, request.FILES)
        if form_data.is_valid():
            form_data.save()
            return redirect('posts_list_views')
        else:
            return render(request, 'blog/post_create_from.html', {"message": "Error in the form"})
    else:
        form=BlogForm()
        return render(request,'blog/post_create_from.html', {'form':form})
    




    