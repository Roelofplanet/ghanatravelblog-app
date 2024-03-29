from django.contrib import admin
from django.urls import path, include  # new
from django.views.generic.base import TemplateView  # new

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),  # new
    path("accounts/", include("django.contrib.auth.urls")),  # new
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("pages/", TemplateView.as_view(template_name="nieuws.html"), name="nieuws"),  # new
    path("posts/", include("posts.urls")),
    path("", include("pages.urls")),
]
