from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="property-index"),
    path("contact", views.contact, name="property-contact")
]
