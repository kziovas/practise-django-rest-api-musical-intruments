from django.contrib import admin
from .models import Instrument, Genre

# Models registered here with administrator.
admin.site.register(Instrument)
admin.site.register(Genre)
