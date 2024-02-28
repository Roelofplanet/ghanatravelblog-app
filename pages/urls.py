from django.contrib import admin
from django.urls import path

from .views import HomePageView, AccomodatiePageView, contactView, successView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("accomodatie/", AccomodatiePageView.as_view(), name="accomodatie"),
    path("contact/", contactView, name="contact"),
    path("success/", successView, name="success"),
]
