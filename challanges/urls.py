from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="challange-index"),
    path("<int:month>", views.monthly_challange_by_number),
    path("<str:month>", views.monthly_challange, name="monthly-challange")
]