from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render, redirect
from .models import Client
from commande.filtre import CommandeFiltre
from client.form import ClientForm
from django.contrib.auth.decorators import  login_required

@login_required(login_url='acces')
def list_client(request, pk):
    client = Client.objects.get(id=pk)
    commandes = client.commande_set.all()
    commandes_total = commandes.count()
    myFilter = CommandeFiltre(request.GET, queryset=commandes)
    commandes = myFilter.qs
    context = {'client' : client,'commandes': commandes, 'commandes_total': commandes_total, 'myFilter': myFilter}
    return render(request, 'client/list_client.html', context)

@login_required(login_url='acces')
def ajouter_client(request):
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/acceuil')
    context = {'form':form}
    return render(request, 'client/ajouter_client.html', context)


@login_required(login_url='acces')
def modifier_client(request, pk):
    client = Client.objects.get(id=pk)
    form = ClientForm(instance=client)
    if request.method == 'POST':
        form = ClientForm(request.POST,instance=client)
        if form.is_valid():
            form.save()
            return redirect('/client' + '/' + pk)
    context = {'form':form}
    return render(request, 'client/ajouter_client.html', context)


@login_required(login_url='acces')
def supprimer_client(request, pk):
    client = Client.objects.get(id=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('/acceuil')
    context = {'client': client}
    return render(request,'client/supprimer_client.html', context)

