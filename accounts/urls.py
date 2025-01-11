from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('register', views.register, name='register'),
    #path('logout', views.logout_views, name='logout'),
    path('sign-out', views.signOut, name='sign_out'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('verify/', views.verify, name='verify'),
    path('forgot_password', views.forgot_password, name='forgot_password'),
    path('reset_password', views.reset_password, name='reset_password'),
]
