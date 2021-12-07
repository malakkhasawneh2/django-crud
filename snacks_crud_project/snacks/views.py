from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView,DeleteView,CreateView,UpdateView
from .models import Snack
from django.urls.base import reverse


# Create your views here.

class SnackCreatView(CreateView):
    template_name='snack_create.html'
    fields=['title','purchaser','description']
    model=Snack

#read
class SnackListView(ListView):
    template_name='snack_list.html'
    model=Snack

class SnackDetailView(DetailView):
    template_name='snack_detail.html'
    model=Snack

#update 
class SnackUpdateView(UpdateView):
    template_name='snack_update.html'
    fields=['title','purchaser','description']
    model=Snack
    

#delete
class SnackDeleteView(DeleteView):
    template_name = "snack_delete.html"
    success_url = reverse_lazy("snack_list")
    model = Snack
    success_url=reverse_lazy('snack_list')