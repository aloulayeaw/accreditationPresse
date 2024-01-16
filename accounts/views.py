from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from dashboard.models import Demande, BanqueImange, BanqueImangePhoto, BanqueRessource
from django.contrib.auth import authenticate, login as auth_login
#from contacts.models import Contact
from .models import CustomUser
from django.contrib.auth import login as auth_login
from django.core.mail import EmailMessage
from django.db.models import Count,Sum

from dashboard.twitter_utils import get_twitter_api
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
            messages.success(request, 'You are now logged in.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
        
    return render(request, 'base/base.html')

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
        profile = request.POST['profile']
        organe = request.POST['organe']

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
                    profile=profile,
                    organe=organe
                )

                if organe != 'Other':
                    # Envoyer un e-mail à "alassane.aw1@ism.edu.sn"
                    subject = 'Demande de connexion'
                    message = f'Le compte a été activé avec succès.\n\n'
                    message += f'Nom: {firstname}\n'
                    message += f'Prénom: {lastname}\n'
                    message += f'Nom d\'utilisateur: {username}\n'
                    message += f'Email: {email}\n'
                    message += f'Profil: {profile}\n'
                    message += f'Organe: {organe}\n'

                    from_email = 'alassane.aw1@ism.edu.sn'  # Remplacez par votre adresse e-mail
                    recipient_list = ['alassane.aw1@ism.edu.sn']
                    email = EmailMessage(subject, message, from_email, recipient_list)
                    email.send()

                elif organe == 'Autre':
                    subject = 'Demande de connexion!'
                    message = f'Le compte a été activé avec succès!.\n\n'
                    message += f'Nom: {firstname}\n'
                    message += f'Prénom: {lastname}\n'
                    message += f'Nom d\'utilisateur: {username}\n'
                    message += f'Email: {email}\n'
                    message += f'Profil: {profile}\n'
                    message += f'Organe: {organe}\n'

                    from_email = 'alassane.aw1@ism.edu.sn'  # Remplacez par votre adresse e-mail
                    recipient_list = ['alassane.aw1@ism.edu.sn']
                    email = EmailMessage(subject, message, from_email, recipient_list)
                    email.send()
                    messages.success(request, 'Votre compte sera activé prochainement.')
                    return redirect('register')

                auth_login(request, user)
                messages.success(request, 'You are now logged in.')
                messages.success(request, 'You are registered successfully.')
                if organe != 'Autre':
                    return redirect('dashboard')
                else:
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
        .values('nbre', 'user__organe')  # Sélectionnez uniquement 'nbre' et 'user__organe'
        .order_by('created_date')
    )
    nbre_data = (
        Demande.objects
        .values('user__organe')  # Sélectionnez uniquement 'user__organe'
        .annotate(total_nbre=Sum('nbre'))  # Calculez la somme de 'nbre' et nommez-la 'total_nbre'
    )
    
    somme_totale = 0

    # Parcourez le queryset et additionnez les valeurs de 'total_nbre'
    for entry in nbre_data:
        somme_totale += entry['total_nbre']
        
    #print(somme_totale)
    # Préparez les données pour le graphique Highcharts
    nbre_values = [entry['nbre'] for entry in pearson_data]
    organe_values = [entry['user__organe'] for entry in pearson_data]

    # consumer_key = 'Rd7iHj3yhLB6ScTz6qJ5TM7tD'
    # consumer_secret = 'Cq71WBN6O1a8xBs8AN8WbfH3XBJKo9KuhnI1Xy0qRtripBY110'
    # access_token = '1538613596-tmMNzbQFMi34UMAgRdlbEgEhrCfFt6f1kvUfM0r'
    # access_token_secret = 'MIqJVxvRauM544KVe3U47MY6MhCDCtDQk9wRjdO46A0Gv'

    # auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    # auth.set_access_token(access_token, access_token_secret)

    # api = tweepy.API(auth)


    # hashtag = 'Appel2023'  # Remplacez par le hashtag que vous souhaitez suivre
    
    # tweet_texts = [] 
    # tweet_dates = [] 
    
    # tweets = tweepy.Cursor(api.search_tweets, q=f'#{hashtag}').items(10)  # Récupérer les 10 derniers tweets avec le hashtag
    # tweet_texts = [tweet.text for tweet in tweets]
    # tweet_dates = [tweet.created_at.strftime('%Y-%m-%d %H:%M:%S') for tweet in tweets]


    # print("tweeets",tweets) 

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

    return render(request, 'accounts/dashboard.html', context)

# def logout(request):
#     if request.method == 'POST':
#         auth.logout(request)
#         return redirect('home')
#     return redirect('home')


def logout_views(request):
    auth.logout(request)
    return redirect('home')




