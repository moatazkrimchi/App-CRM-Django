from django.urls import path
from . import views

urlpatterns = [
    path('/<str:pk>/',views.list_client, name='moataz'),
    path('ajouter_client/',views.ajouter_client, name="ajouter_client"),
    path('/modifier_client/<str:pk>', views.modifier_client, name="modifier_client"),
    path('/supprimer_client/<str:pk>', views.supprimer_client, name="supprimer_client"),

]
