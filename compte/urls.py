from django.urls import path
from . import views

urlpatterns = [
    path('inscription',views.inscriptionPage,name='inscription'),
    path('',views.accesPage,name='acces'),
    path('',views.logoutUser,name='quitter'),
]
