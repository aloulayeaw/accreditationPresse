from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('stats', views.demoOne, name='demo_one'),
    path('dem-rep', views.demoTwo, name='demo_two'),
    path('demo-three', views.demoThree, name='demo_three'),
    path('demande', views.demande, name='demande'),
    path('demandePresse', views.demandePresse, name='demandePresse'),
    path('gallery', views.demoFour, name='demo_four'),
    path('ressources', views.demoFive, name='demo_five'),
    path('demo-six', views.demoSix, name='demo_six'),
    path('demo-seven', views.demoSeven, name='demo_seven'),
    path('demo-eight', views.demoEight, name='demo_eight'),
    path('blog', views.demoNine, name='demo_nine'),
    path('actualite', views.demoTen, name='demo_ten'),
    path('changelog', views.changelog, name='changelog'),
    path('<int:id>', views.presse, name='presse_detail'),
    path('Accepted/', views.presseAccepted, name='presseAccepted'),
    path('Denied/', views.presseDenied, name='presseDenied'),
    path('<int:id>/badge/pdf', views.print_pdf, name="print_badge_pdf",),
]