from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    path("users/", include("allauth.urls")),
    path("livestreams/", include("livestreams.urls")),
    path("products/", include("products.urls")),
]
