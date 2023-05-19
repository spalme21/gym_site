from django.urls import path
from .views import (home, ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView,
                    ClientDeleteView, add_credits)

urlpatterns = [
    path("", home, name="home"),
    path("clients/", ClientListView.as_view(), name="client-list"),
    path("clients/add/", ClientCreateView.as_view(), name="client-add"),
    path("clients/<int:pk>", ClientDetailView.as_view(), name="client-detail-view"),
    path("clients/<int:pk>/update/", ClientUpdateView.as_view(), name="client-update-view"),
    path("clients/<int:pk>/delete/", ClientDeleteView.as_view(), name="client-delete-view"),
    path("clients/<int:pk>/add_credits/", add_credits, name="client-add-credits"),
]
