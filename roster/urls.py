from django.urls import path
from .views import (home, ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView,
                    ClientDeleteView)

urlpatterns = [
    path("", home, name="home"),
    path("clients/", ClientListView.as_view(), name="client-list"),
    path("clients/add/", ClientCreateView.as_view(), name="client-add"),
    path("clients/<int:pk>", ClientDetailView.as_view(), name="client-detail"),
    path("clients/<int:pk>/update/", ClientUpdateView.as_view(), name="client-update"),
    path("clients/<int:pl>/delete/", ClientDeleteView.as_view(), name="client-delete"),
]
