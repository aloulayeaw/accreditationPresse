from django.shortcuts import render
from .models import *
from dashboard.models import Blog
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.

def home(request):
    
    blog = Blog.objects.all()[:2]

    context = {
        'blog': blog,
    }

    return render(request, 'base/base.html', context)

def about(request):

    blog = Blog.objects.all()[:2]

    context = {
        'blog': blog,
    }

    return render(request, 'base/about.html', context)

def blogContent(request):
        
    blog = Blog.objects.all()

    context = {
        'blog': blog,
    }
    return render(request, 'base/blog.html', context)

def gallery(request):
    gallery = Gallery.objects.all()

    paginator = Paginator(gallery, 9)
    page = request.GET.get('page')
    paged_gallery = paginator.get_page(page)

    context = {
        'gallery': gallery,
        'gallery': paged_gallery,
    }

    return render(request, 'base/gallery.html', context)

def designer(request):

    return render(request, 'base/designer.html')


def photographe(request):

    return render(request, 'base/photographe.html')

def developper(request):

    return render(request, 'base/developper.html')

def team(request):

    return render(request, 'base/team.html')

def details(request, id):

    blog= Blog.objects.filter(pk=id).values('tittle','auteur','text','photo','created_date')

    context = {
        'blog': blog
    }

    return render(request, 'base/detailBlog.html', context)