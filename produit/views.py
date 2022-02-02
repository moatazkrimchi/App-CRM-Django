from django.shortcuts import render, redirect
from django.http import HttpResponse
from commande.models import Commande
from client.models import Client
from .models import Tag
from django.contrib.auth.decorators import  login_required
from .form import ProduitForm
from produit.models import Produit

# Create your views here.
@login_required(login_url='acces')
def home(request):
    commandes = Commande.objects.all()
    clients = Client.objects.all()
    context = {'commandes' : commandes,'clients' : clients }

    return render(request,'produit/acceuil.html',context)

@login_required(login_url='acces')
def list_produit(request):
    produits = Produit.objects.all()
    tags = Tag.objects.all()
    context = {'produits' : produits, 'tags': tags}
    return render(request, 'produit/list_produit.html', context)

@login_required(login_url='acces')
def ajouter_produit(request):
    form = ProduitForm()
    if request.method == 'POST':
        form = ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/acceuil/list_produit')
    context = {'form':form}
    return render(request, 'produit/ajouter_produit.html', context)

@login_required(login_url='acces')
def modifier_produit(request, pk):
    produit = Produit.objects.get(id=pk)
    form = ProduitForm(instance=produit)
    if request.method == 'POST':
        form = ProduitForm(request.POST,instance=produit)
        if form.is_valid():
            form.save()
            return redirect('/acceuil/list_produit')
    context = {'form':form}
    return render(request, 'produit/ajouter_produit.html', context)


@login_required(login_url='acces')
def supprimer_produit(request, pk):
    produit = Produit.objects.get(id=pk)
    if request.method == 'POST':
        produit.delete()
        return redirect('/acceuil/list_produit')
    context = {'produit': produit}
    return render(request,'produit/supprimer_produit.html', context)


