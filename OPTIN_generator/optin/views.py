from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import OptINforms
from .models import OptIN, HeaderFooter
from django.contrib import messages 



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
def delete_optin(request, id):
    opt=OptIN.objects.get(id=id)
    opt.delete()
    return redirect('Add_OPTIN')




    