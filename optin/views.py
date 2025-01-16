import csv
from django.shortcuts import render, redirect
from django.http import HttpResponse, response
from .forms import OptINforms
from .models import *
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
        else:
            messages='Enter valid User Name and Password'
            return render(request, 'user.html', {'message':messages})
    return render(request, 'user.html')

@user_passes_test(is_user_authenticated, login_url='userlogin')
def user_logout(request):
    logout(request)
    return redirect('userlogin')



@user_passes_test(is_user_authenticated, login_url='userlogin')
def Add_OPTIN(request):
    if request.method == 'POST':
        # fm = OptINforms(request.POST, request.FILES)
        try:
            user=request.user
            name=request.POST.get('name')
            number=request.POST.get('number')
            email=request.POST.get('email')
            date=request.POST.get('date')
            headerfooter=request.POST.get('header_footer')
            HeaderFooters=HeaderFooter.objects.get(id=headerfooter)
            user_credit=User_account.objects.filter(user=request.user).values('credit')
            if user_credit.exists() and user_credit.first()['credit'] >0:
                fm=OptIN(user=user, name=name, number=number, email=email, data=date, HeaderFooter=HeaderFooters)
                fm.save()
                user_account=User_account.objects.get(user=user)
                user_account.credit -=1
                user_account.save()
                optIn = OptIN.objects.filter(user=request.user)
                headerFooter=HeaderFooter.objects.all()
                return render(request, 'index.html', {"optIn": optIn, 'headerFooter':headerFooter})  # Replace 'success-url' with your actual success URL
            else:
                optIn = OptIN.objects.filter(user=request.user)
                headerFooter = HeaderFooter.objects.all()
                error_message = "You don't have enough credit to perform this action."
                return render(request, 'index.html', {"optIn": optIn, 'headerFooter': headerFooter, 'error': error_message})
        except:
            error='All Form Fields are requered Please fill the from before submiting'
            return render(request, 'index.html', {"error": error})
        
    optIn = OptIN.objects.filter(user=request.user )
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
        header=request.FILES.get('header')
        footer=request.FILES.get('footer')
        headerfooter=HeaderFooter(name=name, header=header, footer=footer)
        headerfooter.save()
        return render(request, 'headerfooter.html',{"message":"header Footer added successfuly"})
    return render(request, 'headerfooter.html')

@user_passes_test(is_user_authenticated, login_url='userlogin')
def upload_csv(request):
    if request.method=="POST":
        user=request.user
        csvfile=request.FILES['file']
        header_footer=request.POST.get('header_footer')
        headerfooter=HeaderFooter.objects.get(id=header_footer)

        def decode_file(file):
            encodings=['utf-8', 'iso-8859-1', 'cp1252']
            for encoding in encodings:
                try:
                    return file.read().decode(encoding).splitlines()
                except UnicodeDecodeError:
                    file.seek(0)
            raise UnicodeDecodeError("Unable to decode the file with the given encodings")

        try:
            # decoded_file = csvfile.read().decode('utf-8').splitlines()
            decoded_file = decode_file(csvfile)
            csv_reader=csv.DictReader(decoded_file)
            row=list(csv_reader)
            count=len(row)
            print(count)
            credit=User_account.objects.filter(user=request.user).values('credit')
            if credit.exists() and credit.first()['credit'] >= count:
                for row in row :
                    optin_data={
                        'user':user,
                        'name':row['Name'],
                        'number':int(row['Number']),
                        'email':row['Email'],
                        'data':row['Date'],
                        'HeaderFooter':headerfooter
                    }
                    OptIN.objects.create(**optin_data)
            else:
                optIn = OptIN.objects.filter(user=request.user)
                headerFooter = HeaderFooter.objects.all()
                error_message = "You don't have enough credit to perform this action."
                return render(request, 'index.html', {"optIn": optIn, 'headerFooter': headerFooter, 'error': error_message})

            user_account=User_account.objects.get(user=request.user)
            user_account.credit -=count
            user_account.save()

            messages.success(request, 'CSV file uploaded successfully.')
            return redirect('messages')  # Redirect to a success page
        except Exception as e:
            messages.error(request, f'Error uploading CSV file: {e}')

    headerFooter = HeaderFooter.objects.all()
    optIn = OptIN.objects.filter(user=request.user)
    return render(request, 'index.html', {'messages': messages.get_messages(request), 'headerFooter': headerFooter, 'optIn':optIn})


@user_passes_test(is_user_authenticated, login_url='userlogin')
def dlt_all(request):
    all_optin=OptIN.objects.filter(user=request.user)
    all_optin.delete()
    return redirect('Add_OPTIN')


@user_passes_test(is_user_authenticated, login_url='userlogin')
def user_profile(request):
    user=request.user
    credits=User_account.objects.filter(user=user)
    return render(request, 'user_profile.html', {'user':user, 'credits':credits})


@user_passes_test(is_user_authenticated, login_url='userlogin')
def template(request):
    optIn = OptIN.objects.filter(user=request.user)
    headerFooter=HeaderFooter.objects.all()
    return render(request, 'template.html', {"optIn": optIn, 'headerFooter':headerFooter}) 


