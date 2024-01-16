from django.shortcuts import render, redirect
from .models import *
from .forms import BanqueImangeForm, DemandeForm, ImagePhotoAddForm, BanqueRessourceForm, BlogForm
from django.db.models import Count, F, ExpressionWrapper, fields
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
import qrcode
import qrcode.image.svg
from io import BytesIO
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

# Create your views here.

def banqueImage(request):
    
    image = BanqueImange.objects.all()

    context = {
        'image': image
    }

    return render(request, 'dashboard/banque_image.html', context)

def banqueImagePhoto(request):
    
    image = BanqueImangePhoto.objects.all()

    context = {
        'image': image
    }

    return render(request, 'dashboard/banque_image_photo.html', context)

def banqueRessource(request):
    
    image = BanqueRessource.objects.all()

    context = {
        'image': image
    }

    return render(request, 'dashboard/banque_image_res.html', context)

def blog(request):
    
    image = Blog.objects.all()

    context = {
        'image': image
    }

    return render(request, 'dashboard/blog.html', context)

# def print_pdf(request, reponse_id):
    # reponse = Demande.objects.get(pk=reponse_id)
    # stream = BytesIO()
    # return render(request, 'dashboard/render.html')

def print_pdf(request, id):
    reponse = Demande.objects.get(pk=id)
    factory = qrcode.image.svg.SvgImage
    img = qrcode.make("http://127.0.0.1:8000/"+"/badge/"+ str(reponse.id) ,image_factory=factory, box_size=20)
    stream = BytesIO()
    img.save(stream) 
    print("print")
    return render(request, 'dashboard/render.html', {'reponse': reponse, 'svg':stream.getvalue().decode()})



def addImage(request):
   #model = Declaration
   userd = request.user.id
   form = BanqueImangeForm
   
   #form = form_class
   if request.method == 'POST' :
      form = BanqueImangeForm(request.POST, request.FILES)
      if form.is_valid() :
         form.save()
         return redirect('banqueImage')
      else:
         form = BanqueImangeForm(request.POST, request.FILES)

def imagePhotoAdd(request):
   #model = Declaration
   userd = request.user.id
   form = ImagePhotoAddForm
   
   #form = form_class
   if request.method == 'POST' :
      form = ImagePhotoAddForm(request.POST, request.FILES)
      if form.is_valid() :
         form.save()
         return redirect('banqueImagePhoto')
      else:
         form = ImagePhotoAddForm(request.POST, request.FILES)


   print(form)

   return render(request, 'dashboard/image_add_photo.html', {'form'  : form, 'userd': userd})

def banqueRessourceAdd(request):
   #model = Declaration
   userd = request.user.id
   form = BanqueRessourceForm
   
   #form = form_class
   if request.method == 'POST' :
      form = BanqueRessourceForm(request.POST, request.FILES)
      if form.is_valid() :
         form.save()
         return redirect('banqueImagePhoto')
      else:
         form = BanqueRessourceForm(request.POST, request.FILES)

   return render(request, 'dashboard/image_add_res.html', {'form'  : form, 'userd': userd})


def blogAdd(request):
   #model = Declaration
   form = BlogForm
   
   #form = form_class
   if request.method == 'POST' :
      form = BlogForm(request.POST, request.FILES)
      if form.is_valid() :
         form.save()
         return redirect('blog')
      else:
         form = BlogForm(request.POST, request.FILES)

   return render(request, 'dashboard/blog_add.html', {'form'  : form})


def ressource(request):

   return render(request, 'dashboard/ressource.html')

def gallery(request):

   return render(request, 'dashboard/gallery.html')


#@login_required 
def viewImage(request):
    banqueImg = BanqueImange.objects.all()

    context = {
        'banqueImg': banqueImg,
    }

    return render(request, 'dashboard/view_image.html', context)


def viewImagePhoto(request):
    banqueImg = BanqueImangePhoto.objects.all()

    context = {
        'banqueImg': banqueImg,
    }

    return render(request, 'dashboard/view_photo.html', context)


def delete(request, id):
    bimg = BanqueImange.objects.get(id=id)
    bimg.delete()
    return redirect('banqueImage')

def deletephoto(request, id):
    bimg = BanqueImangePhoto.objects.get(id=id)
    bimg.delete()
    return redirect('banqueImagePhoto')

def deleteres(request, id):
    bimg = BanqueRessource.objects.get(id=id)
    bimg.delete()
    return redirect('banqueRessource')

def deleteblog(request, id):
    bimg = Blog.objects.get(id=id)
    bimg.delete()
    return redirect('blog')

def demande(request):
   #model = Declaration
   userd=request.user.id
   form = DemandeForm
   
   #form = form_class
   if request.method == 'POST' :
      form = DemandeForm(request.POST, request.FILES)
      if form.is_valid() :
         form.save()
        #  subject = 'Nouvelle Demande'
        #  message_text = f'Nouvelle Demande, veillez-vous connecter'
        #  from_email = 'alassane.aw1@ism.edu.sn'  # Remplacez par votre propre adresse e-mail
        #  recipient_list = ['alassane.aw1@ism.edu.sn']  # Adresse e-mail de destination
        #  send_mail(subject, message_text, from_email, recipient_list, fail_silently=False)
         
         return redirect('dashboard')
      else:
         form = DemandeForm(request.POST, request.FILES)

    
   dempresse = Demande.objects.filter(statut="Accepted").count

   return render(request, 'dashboard/demande.html', {'form'  : form, 'userd': userd, 'dempresse': dempresse})


def demandePresse(request):
    
    demande = Demande.objects.all()

    context = {
        'demande': demande
    }

    return render(request, 'dashboard/demande_presse.html', context)

def reponse(request):
    
    demand = Demande.objects.filter(statut="Accepted")
    dempresse = Demande.objects.filter(statut="Accepted").count

    context = {
        'demand': demand,
        'dempresse': dempresse
    }

    return render(request, 'dashboard/reponse.html', context)


def presse(request, id):
    
    presse_detail = get_object_or_404(Demande, pk=id)

    context = {
        'presse_detail': presse_detail
    }

    return render(request, 'dashboard/presse_detail.html', context)



def presseviews(request):
    

    return render(request, 'dashboard/presse.html')


def presseAccepted(request, id):
    demande = Demande.objects.get(pk=id)
    demande.statut="Accepted"
    demande.save()

    return redirect('dashboard')


def presseDenied(request, id):
    demande = Demande.objects.get(pk=id)
    demande.statut="denied"
    demande.save()

    return redirect('dashboard')
