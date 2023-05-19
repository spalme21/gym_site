from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Client

def home(request):
    """View function for the home page."""
    return render(request, "roster/home.html")

class ClientListView(LoginRequiredMixin, ListView):
    """Generic view for a list of clients."""
    model = Client
    paginate_by = 20

class ClientDetailView(LoginRequiredMixin, DetailView):
    """Generic view to view details about a client."""
    model = Client

class ClientCreateView(LoginRequiredMixin, CreateView):
    """Generic view to create a new client."""
    model = Client
    fields = ["last_name", "first_name", "email"]

class ClientUpdateView(LoginRequiredMixin, UpdateView):
    """Generic view to update an existing client."""
    model = Client
    fields = ["last_name", "first_name", "email"]

class ClientDeleteView(LoginRequiredMixin, DeleteView):
    """Generic view to delete a client."""
    model = Client
    success_url = reverse_lazy("client-list")
