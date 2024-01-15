from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import OptINforms
from .models import OptIN, HeaderFooter
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test


def is_user_authenticated(user):
    return user.is_authenticated

def userlogin(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Add_OPTIN') 
    return render(request, 'user.html')
   

def user_logout(request):
    logout(request)
    return redirect('userlogin')



@user_passes_test(is_user_authenticated, login_url='userlogin')
def Add_OPTIN(request):
    if request.method == 'POST':
        # fm = OptINforms(request.POST, request.FILES)
        try:
            name=request.POST.get('name')
            number=request.POST.get('number')
            email=request.POST.get('email')
            date=request.POST.get('date')
            headerfooter=request.POST.get('header_footer')
            print(headerfooter)
            HeaderFooters=HeaderFooter.objects.get(id=headerfooter)
            print(HeaderFooter)
            fm=OptIN(name=name, number=number, email=email, data=date, HeaderFooter=HeaderFooters)
            
            fm.save()
                
            optIn = OptIN.objects.all()
            headerFooter=HeaderFooter.objects.all()
            return render(request, 'index.html', {"optIn": optIn, 'headerFooter':headerFooter})  # Replace 'success-url' with your actual success URL
        except:
            error='All Form Fields are requered Please fill the from before submiting'
            return render(request, 'index.html', {"error": error})           
    

    optIn = OptIN.objects.all()
    headerFooter=HeaderFooter.objects.all()
    return render(request, 'index.html', {"optIn": optIn, 'headerFooter':headerFooter})

        

#delete optin
@user_passes_test(is_user_authenticated, login_url='userlogin')
def delete_optin(request, id):
    opt=OptIN.objects.get(id=id)
    opt.delete()
    return redirect('Add_OPTIN')



@user_passes_test(is_user_authenticated, login_url='userlogin')
def headerfooter(request):
    if request.method=="POST":
        name=request.POST.get('name')
        header=request.POST.get('header')
        footer=request.POST.get('footer')
        headerfooter=HeaderFooter(name=name, header=header, footer=footer)
        headerfooter.save()
        return HttpResponse('add successfully', 'headerfooter.html')    
    return render(request, 'headerfooter.html')

    