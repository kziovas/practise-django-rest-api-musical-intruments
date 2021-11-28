from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/instruments",
        include("Instruments.routing.instruments_urls", namespace="instrument_api"),
    ),
]
