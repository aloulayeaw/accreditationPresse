
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('gallery', views.gallery, name='gallery'),
    path('designer', views.designer, name='designer'),
    path('developper', views.developper, name='developper'),
    path('photographe', views.photographe, name='photographe'),
    path('blogContent', views.blogContent, name='blogContent'),
    path('team', views.team, name='team'),
    path('details/<int:id>', views.details , name='details'),
]
