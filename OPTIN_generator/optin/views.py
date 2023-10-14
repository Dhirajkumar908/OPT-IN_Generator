from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import OptINforms
from .models import OptIN


def Add_OPTIN(request):
    if request.method == 'POST':
        fm = OptINforms(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
            
            optIn = OptIN.objects.all()
            return render(request, 'index.html', {"form": fm, "optIn": optIn})  # Replace 'success-url' with your actual success URL
    else:
        fm = OptINforms()

    optIn = OptIN.objects.all()
    return render(request, 'index.html', {"form": fm, "optIn": optIn})

        

#delete optin
def delete_optin(request, id):
    opt=OptIN.objects.get(id=id)
    opt.delete()
    return redirect('Add_OPTIN')




    