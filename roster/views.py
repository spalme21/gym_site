from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (CreateView, DeleteView, UpdateView,
                                       FormView)
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import Client, ClassSession
from .forms import ChangeCreditsModelForm

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

@login_required
def add_credits(request, pk):
    """View function to add credits to a client."""
    client = get_object_or_404(Client, pk=pk)

    if request.method == "POST":
        form = ChangeCreditsModelForm(request.POST)

        if form.is_valid():
            client.credits += form.cleaned_data["credits"]
            client.save()

            return HttpResponseRedirect(client.get_absolute_url())

    else:
        form = ChangeCreditsModelForm(initial={"credits": 0})

    context = {
        "form": form,
        "client": client,
    }

    return render(request, "roster/client_add_credits.html", context)

class ClassSessionFormView(LoginRequiredMixin, FormView):
    """Generic view for a form to schedule a class."""
    model = ClassSession
    fields = ["class_type", "date_and_time", "roster"]