from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from dashboard.models import Demande, BanqueImange, BanqueImangePhoto, BanqueRessource
from django.contrib.auth import authenticate, login as auth_login
#from contacts.models import Contact
from .models import CustomUser, VerificationCode
from django.contrib.auth import login as auth_login,logout
from django.core.mail import EmailMessage
from django.db.models import Count,Sum
#from .models import CustomUser, VerificationCode
import random
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
#from dashboard.twitter_utils import get_twitter_api
import tweepy

# Create your views here.

def login(request):
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']
        print("login",email,password)

        user = auth.authenticate(email=email, password=password)
        print("user",user)
        
        if user is not None:
            auth.login(request, user)
            #messages.success(request, 'You are now logged in.')
            return redirect('dashboard/stats')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
        
    return render(request, 'auth/login.html')

# def login(request):
#     if request.method == 'POST':
#         email = request.POST['username']
#         password = request.POST['password']

#         # Vous n'avez pas besoin de la fonction authenticate ici

#         # Vérifiez les informations d'identification manuellement
#         user = CustomUser.objects.filter(email=email).first()
        
#         if user is not None and user.check_password(password):
#             print("user", user)
#             # Connectez l'utilisateur manuellement en définissant l'ID de l'utilisateur dans la session
#             request.session['user_id'] = user.id
#             #messages.success(request, 'You are now logged in.')
#             return redirect('dashboard')
#         else:
#             messages.error(request, 'Invalid login credentials')
#             return redirect('login')

#     return render(request, 'base/base.html')


def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        profile = "presse"
        organe = request.POST['organe']
        profile_organe = request.POST['profile_organe']
        print("organe",organe)
        if organe == "Autre":
            organe = request.POST['other_organe']
        else:
            organe = request.POST['organe']
            
        print("data",firstname,lastname,username,email,password,profile,organe,profile_organe)
        
        if password == confirm_password:
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists!')
                return redirect('register')
            elif CustomUser.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists!')
                return redirect('register')
            else:
                # Create a user but set `is_active` to False for verification
                user = CustomUser.objects.create_user(
                    first_name=firstname,
                    last_name=lastname,
                    email=email,
                    username=username,
                    password=password,
                    profile=profile,
                    organe=organe,
                    profile_organe=profile_organe,
                    is_active=False
                )
                
                # Generate a 6-digit verification code
                verification_code = random.randint(100000, 999999)
                # Save the verification code to the database
                VerificationCode.objects.create(user=user, code=verification_code)
                # Send the verification code to the user's email
                subject = 'Activez votre compte'
                message = f'Bonjour {firstname},\n\nUtilisez le code suivant pour activer votre compte:\n\n{verification_code}\n\nThank you!'
                email = EmailMessage(subject, message, 'your-email@example.com', [email])
                email.send()
                
                messages.success(request, 'Un email vous a été envoyé avec un code de vérification.')
                return redirect('verify') 
        else:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')
    else:
        return render(request, 'auth/register.html')


def verify(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        code = request.POST.get('code')

        try:
            verification = VerificationCode.objects.get(user__email=email, code=code)
            user = verification.user
            user.is_active = True
            user.save()
            verification.delete()
            messages.success(request, 'Votre compte a été activé. Vous pouvez maintenant vous connecter.')
            return redirect('login')
        except VerificationCode.DoesNotExist:
            messages.error(request, 'Invalid verification code or email.')
            return redirect('verify')
    return render(request, 'auth/verify.html')

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        try:
            user = CustomUser.objects.get(email=email)  # CustomUser instead of User
            reset_code = get_random_string(length=6, allowed_chars='0123456789')

            user.reset_code = reset_code
            user.save()

            subject = 'Réinitialisez votre mot de passe'
            message = f'Bonjour  {user.first_name},\n\nVoici le code pour réinitialiser votre mot de passe :  {reset_code}\n\nMerci!'
            send_mail(subject, message, 'mamerane1003@gmail.com', [email])
            
            messages.success(request, 'Un code de réinitialisation a été envoyé à votre adresse e-mail.')
            return redirect('reset_password')
        except CustomUser.DoesNotExist:
            messages.error(request, 'Aucun utilisateur trouvé avec cette adresse e-mail.')
            return redirect('forgot_password')
    return render(request, 'auth/forget.html')

def reset_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        reset_code = request.POST['reset_code']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        try:
            user = CustomUser.objects.get(email=email, reset_code=reset_code)
            if new_password == confirm_password:
                user.set_password(new_password)
                user.reset_code = None  # Clear the reset code after successful reset
                user.save()
                messages.success(request, 'Votre mot de passe a été réinitialisé avec succès.')
                return redirect('login')
            else:
                messages.error(request, 'Les mots de passe ne correspondent pas.')
        except CustomUser.DoesNotExist:
            messages.error(request, 'Code de réinitialisation ou e-mail invalide.')
    return render(request, 'auth/reset_password.html')

@login_required(login_url = 'login')
def dashboard(request):
    #user_inquiry = Contact.objects.order_by('-create_date').filter(user_id=request.user.id)
    # count = Contact.objects.order_by('-create_date').filter(user_id=request.user.id).count()
    user = request.user
    #Presse
    response = Demande.objects.filter(statut="Accepted").count()
    res = Demande.objects.all().count()
    
    demandes_user = Demande.objects.filter(user=user).count()
    
    demandes_user_stat = Demande.objects.filter(user=user,statut="Accepted").count()


    #Designer
    baqnueImg = BanqueImange.objects.all().count() 
    imagePhoto = BanqueImangePhoto.objects.all().count()
    resource = BanqueRessource.objects.all().count()

    pearson_data = (
        Demande.objects
        .filter(statut="Accepted").values('nbre', 'user__organe') 
        .order_by('created_date')
    )
    nbre_data = (
        Demande.objects
        .filter(statut="Accepted").values('user__organe') 
        .annotate(total_nbre=Sum('nbre')) 
    )
    
    somme_totale = 0

    for entry in nbre_data:
        somme_totale += entry['total_nbre']
        
    nbre_values = [entry['nbre'] for entry in pearson_data]
    organe_values = [entry['user__organe'] for entry in pearson_data]


    context = {
        'response': response,
        'baqnueImg': baqnueImg,
        'imagePhoto': imagePhoto,
        'resource': resource,
        'res':res,
        'nbre_values': nbre_values,
        'organe_values':organe_values,
        'somme_totale':somme_totale,
        'demandes_user':demandes_user,
        'demandes_user_stat':demandes_user_stat,
    }

    return render(request, 'auth/forget.html', context)



# def logout(request):
#     if request.method == 'POST':
#         auth.logout(request)
#         return redirect('home')
#     return redirect('home')


@login_required
def signOut(request):
    logout(request)
    return redirect('login')




