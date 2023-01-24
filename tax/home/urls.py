from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_home_page, name="mainH"),
    path('login/', views.signInView, name="login"),  
    path('dash/<int:id>/', views.dash, name='dash'),
    path('signout/', views.signOut, name='logout'),
    path('contactus/', views.contact_page, name="contact"),
]
