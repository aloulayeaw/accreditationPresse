from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import DemandeForm
from django.db.models import Count, F, ExpressionWrapper, fields
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
import qrcode
import qrcode.image.svg
from io import BytesIO
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.http import JsonResponse
from django.db.models import Count
from django.contrib import messages
from email.mime.image import MIMEImage 
import base64
from django.urls import reverse
from django.core.mail import send_mail
from django.db import connection
from django.db.models import Q
from django.db.models import Count,Sum
import json
from django.views.decorators.csrf import csrf_exempt
from collections import Counter

# demo one dashboard page
@login_required
def demoOne(request):
    
    user = request.user
    userd = request.user.id
    
    profile = CustomUser.objects.filter(id=userd).values_list('profile', flat=True).first()
    print("Profile :", profile)
    
    if profile == "groupecentrale":        
        demande = Demande.objects.all()
        demandes_user = Demande.objects.filter().count()
        demandes_user_stat = Demande.objects.filter(statut="Accepted").count()
        
    elif profile != "groupecentrale":
        demande = Demande.objects.all()
        demandes_user = Demande.objects.filter(user=user).count()
        
        demandes_user_stat = Demande.objects.filter(user=user,statut="Accepted").count()
    else:
        demande = None 

    demande_waitting= demandes_user - demandes_user_stat
    #print('demande_waitting',demande_waitting)
       
    #demande = Demande.objects.filter(user=user)
    #demandes_user = Demande.objects.filter(user=user).count()
    
    #demandes_user_stat = Demande.objects.filter(user=user,statut="Accepted").count()

    #print('dem',demande)
    
    pearson_data = (
        Demande.objects
        .filter(statut="Accepted").values('nbre', 'user__organe','user__profile_organe') 
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

    grouped_data = Counter()
    for entry in pearson_data:
        profile_organe = entry['user__profile_organe']
        nbre = entry['nbre']
        grouped_data[profile_organe] += nbre

    organe_values_profile = list(grouped_data.keys())  # Les profils uniques
    nbre_values = list(grouped_data.values()) 
       
    total_dem=Demande.objects.filter(statut="Accepted").aggregate(total_nbre=Sum('nbre'))['total_nbre'] or 0

    nbre_values = [entry['nbre'] for entry in pearson_data]
    organe_values = [entry['user__organe'] for entry in pearson_data]  
    
    organe_values_profile = [entry['user__profile_organe'] for entry in pearson_data]  
    
    context = {
        'demande': demande,
        'demandes_user':demandes_user,
        'demandes_user_stat':demandes_user_stat,
        'demande_waitting': demande_waitting,
        'somme_totale':somme_totale,
        'nbre_values': nbre_values,
        'organe_values':organe_values,
        'nbre_values': nbre_values,
        'organe_values_profile': organe_values_profile,
        'total_dem':total_dem,
    }

    return render(request, 'pages/dashboards/demo_one.html', context)

# demo two dashboard page
@login_required
def demoTwo(request):
    
    userd = request.user.id
    dempresse = Demande.objects.filter(user=userd).count()
    print('dempresse',dempresse)
    profile = CustomUser.objects.filter(id=userd).values_list('profile', flat=True).first()
    print("Profile :", profile)
    if profile == "groupecentrale":
        demande = Demande.objects.all()
    elif profile == "presse":
        demande = Demande.objects.filter(user=userd)
    else:
        demande = None 
    

    context = {
        'dempresse': dempresse,
        'demande': demande
    }
    
    return render(request, 'pages/dashboards/demo_two.html',context)

# demo three dashboard page
@login_required
def demoThree(request):
    query = request.GET.get('query', '').strip()
    print("query",query)
    if query=="En Attente":
        query="publié"
    
    if query=='':
        demandes = Demande.objects.all()
        
    demandes = Demande.objects.all()


    if query and len(query) > 2:
        demandes = demandes.filter(
            Q(user__organe__icontains=query) | Q(statut__icontains=query)
        )
        
    context = {
        'demande': demandes,
        'query': query,
    }
    
    return render(request, 'pages/dashboards/demo_three.html', context)
    


# demo four dashboard page
@login_required
def demoFour(request):
    return render(request, 'pages/dashboards/demo_four.html')

# demo five dashboard page
@login_required
def demoFive(request):
    return render(request, 'pages/dashboards/demo_five.html')

# demo six dashboard page
@login_required
def demoSix(request):
    return render(request, 'pages/dashboards/demo_six.html')

# demo seven dashboard page
@login_required
def demoSeven(request):
    return render(request, 'pages/dashboards/demo_seven.html')

# demo eight dashboard page
@login_required
def demoEight(request):
    return render(request, 'pages/dashboards/demo_eight.html')

# demo nine dashboard page
@login_required
def demoNine(request):
    return render(request, 'pages/dashboards/demo_nine.html')

# demo ten dashboard page
@login_required
def demoTen(request):
    return render(request, 'pages/dashboards/demo_ten.html')

# changelog page
@login_required
def changelog(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        service = request.POST.get('service')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message_content = request.POST.get('message')

        if not name or not email or not message_content:
            messages.error(request, "Veuillez remplir tous les champs requis.")
            return HttpResponseRedirect(reverse('dashboard:changelog'))

        if service == "Commission Scientifique":
            recipient_list = ['mamerane1003@gmail.com']
        elif service == "Commission Communication":
            recipient_list = ['babacar.sow@senelec.sn']
        elif service == "Support":
            recipient_list = ['mamerane1003@gmail.com']
        else:
            messages.error(request, "Service inconnu. Veuillez choisir un service valide.")
            return HttpResponseRedirect(reverse('dashboard:changelog'))

        subject = f"Message de {name} - Service: {service}"
        message = f"Nom: {name}\nService: {service}\nEmail: {email}\nTéléphone: {phone}\n\nMessage:\n{message_content}"
        from_email = 'no-reply@ac-presse.com'

        try:
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            messages.success(request, "Votre message a été envoyé avec succès.")
        except Exception as e:
            messages.error(request, f"Une erreur s'est produite: {str(e)}")

        return HttpResponseRedirect(reverse('dashboard:changelog'))

    return render(request, 'pages/changelog/changelog.html')



def print_pdf(request, id):
    try:
        # Get the current user
        userd = request.user.id
        reponse = get_object_or_404(Demande, pk=id)

        # Generate QR Code
        qr = qrcode.QRCode(box_size=10)
        #qr.add_data(f"Accreditation for {reponse.nom}")
        qr.add_data(f"https://accreditation-presse.com/fr/dashboard/badge/{reponse.id}")
        qr.make(fit=True)
        img = qr.make_image(fill_color="green", back_color="white")
        stream = BytesIO()
        img.save(stream, format="PNG")  # Save QR code as PNG
        qr_code_image = stream.getvalue()

        # Prepare Email Content
        subject = 'Groupement Centrale Layenne'
        message = f"""
        <html>
            <body>
                <p>Bonjour <strong>M/Mme {reponse.nom}</strong>,</p>
                <p>Comme stipulé sur le dernier mail, le retrait des badges se fera à partir du … à … . Pour vous y rendre plus facilement cliquez ici pour avoir la géolocalisation.</p>
                <p>Il est noté aussi que pour des raisons de sécurité, le retrait se fera via un Code QR que devra présenter le responsable de la demande ou la personne mandaté par l’organe en question pour le retrait de ses badges.</p>
                <p>Ce QR est envoyé en pièce jointe de ce mail.</p>
                <p>Si vous avez des questions supplémentaires ou des besoins n’hésitez pas à nous contacter. Nous sommes là pour vous aider et faciliter votre travail de reportage.</p>
                <img src="cid:qr_code_image" alt="QR Code" style="width: 250px; height: 250px;">
                <p>Veuillez agréer, chers membres de la presse, nos salutations les plus respectueuses</p>
                <p><strong>Commission Communication Groupement Cenectrale Layenne</strong></p>
            </body>
        </html>
        """

        from_email = 'alassane.aw1@ism.edu.sn'
        recipient_list = [reponse.email]

        # Create and send the email with the QR code as an inline image
        email = EmailMessage(subject, message, from_email, recipient_list)
        email.content_subtype = "html"  # Specify that the email content is HTML

        # Attach the QR code image as inline
        mime_image = MIMEImage(qr_code_image, _subtype="png")
        mime_image.add_header('Content-ID', '<qr_code_image>')
        mime_image.add_header('Content-Disposition', 'inline', filename="qr_code.png")
        email.attach(mime_image)

        email.send()
        qr_code_base64 = base64.b64encode(qr_code_image).decode('utf-8')
        # Render Response
        return render(request, 'pages/dashboards/render.html', {'reponse': reponse, 'qr_code_svg': f"data:image/png;base64,{qr_code_base64}"})

    except Demande.DoesNotExist:
        # Handle case where the demand does not exist
        messages.error(request, "La demande n'existe pas.")
        return redirect('dashboard:demo_one')

    except Exception as e:
        # Handle general exceptions
        print(f"Une erreur s'est produite: {str(e)}")
        return redirect('dashboard:demo_one')

def demande(request):
    userd = request.user.id
    print('User',userd)
    organe = Demande.objects.filter(user=userd).values_list('user__organe', flat=True).distinct()[:0]
    print("organe",organe)
    dempresse = Demande.objects.filter(user=userd).count
    print('dempresse',dempresse)

    if request.method == 'POST':
        # Capture data manually
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        adresse = request.POST.get('adresse')
        telephone = request.POST.get('telephone')
        nbre = request.POST.get('nbre')
        pearson = request.POST.get('pearson')
        responsable = request.POST.get('responsable')
        comments = request.POST.get('comments')
        link_intagram = request.POST.get('link_intagram')
        link_website = request.POST.get('link_website')
        
        if link_intagram is not None:
            link_intagram = request.POST.get('link_intagram')
            
        if link_website is not None:
            link_website = request.POST.get('link_website')
        statut = 'publié'
            
        names_list = pearson.split(',') if pearson else []
        
        # Save the data to the model
        demande = Demande(
            nom=nom,
            email=email,
            adresse=adresse,
            telephone=telephone,
            nbre=nbre,
            pearson=pearson,
            responsable=responsable,
            comments=comments,
            statut=statut,
            link_intagram=link_intagram,
            link_website=link_website,
            user_id=userd,
        )
        demande.save()

        # Send email notification
        subject = 'Demande Accréditation'
        message = """\
        Cher(e) partenaire,

        Nous accusons réception de votre demande d’accréditation dans la plateforme **Appel 2025**. 
        Votre demande a été bien enregistrée et est actuellement en cours de traitement. 

        Nous vous tiendrons informé(e) dès que le traitement sera finalisé.

        Nous vous remercions pour l’intérêt que vous portez à la couverture de l’Appel de Seydina Limamou Lahi (PSL).

        La Commission Communication
        """

        from_email = 'alassane.aw1@ism.edu.sn'
        recipient_list = [email]
        email = EmailMessage(subject, message, from_email, recipient_list)
        email.send()

        return redirect('dashboard:demo_one')

    return render(request, 'components/dashboard/demo_two/revenue_source.html', {'userd': userd, 'dempresse': dempresse})


@login_required
def demandePresse(request):
    userd = request.user.id
    print("user",userd)
    query = request.GET.get('query', '').strip()
    print('query',query)
    profile = CustomUser.objects.filter(id=userd).values_list('profile', flat=True).first()
    print("Profile :", profile)
    if profile == "groupecentrale":
        if query:  # Si une requête est fournie
            demande = Demande.objects.filter(
                Q(user__organe__icontains=query) |
                Q(statut__icontains=query) |
                Q(user__profile_organe__icontains=query)
            )
        else: 
            demande = Demande.objects.all()
    elif profile == "presse":
        demande = Demande.objects.filter(user=userd)
    else:
        demande = None 
    
    context = {
        'demande': demande
    }

    return render(request, 'pages/dashboards/demo_three.html', context)


@csrf_exempt
@login_required
def presseAccepted(request):
    try:
        data = json.loads(request.body)
        user_id = data.get("user_id")
        new_nbre = data.get("new_nbre", None)
    
        demande = Demande.objects.get(user_id=user_id)
        if new_nbre is not None:
            demande.nbre = new_nbre

        demande.statut = "Accepted"
        demande.save()

        # Generate QR Code as PNG
        qr_code = qrcode.QRCode(box_size=10, border=4)
        qr_code.add_data(f"https://accreditation-presse.com/fr/dashboard/badge/{demande.id}")
        qr_code.make(fit=True)

        # Create a PNG image
        img = qr_code.make_image(fill_color="green", back_color="white")
        stream = BytesIO()
        img.save(stream, format="PNG")
        qr_code_png = stream.getvalue()

        # Prepare email content
        subject = 'Réponse Commission Communication Layéne'
        html_content = f"""
        <html>
            <body>
                <p>Laye Makhtar, Cher Partenaire,</p>
                <p>La commission Communication de l’Appel de Seydina Limamou Laye (Psl) vous remercie de l’intérêt que vous portez pour la couverture et au succès de cet évènement.</p>
                <p>Après traitement, la Commission a retenu de vous octroyer <strong>{demande.nbre}</strong> badges à votre organe.</p>
                <p>Pour des raisons de sécurité, vous pouvez aussi télécharger vos badges suivant le QR Code ci-joint.</p>
                <p>Le retrait des badges se fera à partir du … ……………..à ………………, veuillez contacter :</p>
                <p><strong>• Fatou Laye Mbaye : 77 640 60 32</strong></p>
                <p><strong>• Babacar SOW : 77 333 38 89</strong></p>
                <p><strong>• Abibou DIOP : 77 727 26 84</strong></p>
                <p>Voici votre QR Code d'accréditation :</p>
                <img src="cid:qr_code_image" alt="QR Code" style="width: 250px; height: 250px;">
                <p>La Commission Communication,</p>
            </body>
        </html>
        """

        from_email = 'alassane.aw1@ism.edu.sn'
        recipient_list = [demande.email]

        # Send the email with embedded image
        email = EmailMultiAlternatives(subject, html_content, from_email, recipient_list)
        email.attach_alternative(html_content, "text/html")

        # Attach the QR Code as a PNG image
        image = MIMEImage(qr_code_png, _subtype="png")
        image.add_header('Content-ID', '<qr_code_image>')
        image.add_header('Content-Disposition', 'inline', filename="qr_code.png")
        email.attach(image)

        email.send()

        return JsonResponse({"success": True, "message": "Demande acceptée avec succès."})

    except Demande.DoesNotExist:
        return JsonResponse({"success": False, "message": "Demande non trouvée."}, status=404)

    except Exception as e:
        print("Erreur:", e)
        return JsonResponse({"success": False, "message": str(e)}, status=500)


def presseDenied(request, id):
    demande = Demande.objects.get(pk=id)
    demande.statut="denied"
    demande.save()

    return redirect('dashboard:demo_one')
