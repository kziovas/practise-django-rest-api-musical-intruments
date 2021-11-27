from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('Instruments.routing.instruments_urls', namespace='instrument_api'))
]
