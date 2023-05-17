from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import render

from .models import Client

def home(request):
    """View function for the home page."""
    return render(request, "home.html")

class ClientListView(ListView):
    """Generic view for a list of clients."""
    model = Client

class ClientDetailView(DetailView):
    """Generic view to view details about a client."""
    model = Client

class ClientCreateView(CreateView):
    """Generic view to create a new client."""
    model = Client
    fields = ["last_name", "first_name", "email"]

class ClientUpdateView(UpdateView):
    """Generic view to update an existing client."""
    model = Client
    fields = ["last_name", "first_name", "email"]

class ClientDeleteView(DeleteView):
    """Generic view to delete a client."""
    model = Client
    success_url = reverse_lazy("client-list")
