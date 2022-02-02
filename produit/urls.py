from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='acceuil'),
    path('ajouter_produit/',views.ajouter_produit, name="ajouter_produit"),
    path('/list_produit/',views.list_produit, name="list_produit"),
    path('modifier_produit/<str:pk>', views.modifier_produit, name="modifier_produit"),
    path('/supprimer_produit/<str:pk>', views.supprimer_produit, name="supprimer_produit"),

]
