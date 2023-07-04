from django.contrib import admin
from django.urls import path

from .views import HomePageView, NieuwsPageView, contactView, successView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("nieuws/", NieuwsPageView.as_view(), name="nieuws"),
    path("contact/", contactView, name="contact"),
    path("success/", successView, name="success"),
]
