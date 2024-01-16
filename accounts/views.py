from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from dashboard.models import Demande, BanqueImange, BanqueImangePhoto, BanqueRessource
#from contacts.models import Contact
from .models import CustomUser
from django.contrib.auth import login as auth_login

# Create your views here.

def login(request):
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']
        print("login",email,password)

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
        
    return render(request, 'base/base.html')

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        profile = request.POST['profile']

        if password == confirm_password:
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists!')
                return redirect('register')
            elif CustomUser.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists!')
                return redirect('register')
            else:
                user = CustomUser.objects.create_user(
                    first_name=firstname,
                    last_name=lastname,
                    email=email,
                    username=username,
                    password=password,
                    profile=profile
                )
                auth_login(request, user)
                messages.success(request, 'You are now logged in.')
                messages.success(request, 'You are registered successfully.')
                return redirect('login')
        else:
            messages.error(request, 'Password do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')
    
    
@login_required(login_url = 'login')
def dashboard(request):
    #user_inquiry = Contact.objects.order_by('-create_date').filter(user_id=request.user.id)
    # count = Contact.objects.order_by('-create_date').filter(user_id=request.user.id).count()

    #Presse
    response = Demande.objects.filter(statut="Accepted").count()

    #Designer
    baqnueImg = BanqueImange.objects.all().count() 
    imagePhoto = BanqueImangePhoto.objects.all().count()
    resource = BanqueRessource.objects.all().count()

    context = {
        'response': response,
        'baqnueImg': baqnueImg,
        'imagePhoto': imagePhoto,
        'resource': resource
    }

    return render(request, 'accounts/dashboard.html', context)

# def logout(request):
#     if request.method == 'POST':
#         auth.logout(request)
#         return redirect('home')
#     return redirect('home')


def logout_views(request):
    auth.logout(request)
    return redirect('home')




