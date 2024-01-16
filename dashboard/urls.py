
from django.urls import path
from . import views

urlpatterns = [
    path('banqueImage', views.banqueImage, name='banqueImage'),
    path('addImage', views.addImage, name='addImage'),
    path('banqueImagePhoto', views.banqueImagePhoto, name='banqueImagePhoto'),
    path('blog', views.blog, name='blog'),
    path('blogAdd', views.blogAdd, name='blogAdd'),
    path('pearson_chart_data/', views.pearson_chart_data, name='pearson_chart_data'),
    path('imagePhotoAdd', views.imagePhotoAdd, name='imagePhotoAdd'),
    path('banqueRessource', views.banqueRessource, name='banqueRessource'),
    path('banqueRessourceAdd', views.banqueRessourceAdd, name='banqueRessourceAdd'),
    path('ressource', views.ressource, name='ressource'),
    path('demande', views.demande, name='demande'),
    path('gallerie', views.gallery, name='gallerie'),
    path('viewImage', views.viewImage, name='viewImage'),
    path('viewImagePhoto', views.viewImagePhoto, name='viewImagePhoto'),
    path('delete/<int:id>', views.deletephoto , name='deletephoto'),
    path('delete/<int:id>', views.delete , name='delete'),
    path('delete/<int:id>', views.deleteres , name='deleteres'),
    path('delete/<int:id>', views.deleteblog , name='deleteblog'),
    path('demandePresse', views.demandePresse, name='demandePresse'),
    path('presseviews', views.presseviews, name='presseviews'),
    path('<int:id>', views.presse, name='presse_detail'),
    path('Accepted/<str:id>', views.presseAccepted , name='presseAccepted'),
    path('Denied/<str:id>', views.presseDenied , name='presseDenied'),
    path('reponse', views.reponse , name='reponse'),
    path('<int:id>/badge/pdf', views.print_pdf, name="print_badge_pdf",),
]
