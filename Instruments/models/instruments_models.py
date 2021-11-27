import uuid
import datetime
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# The app models live here
class Genre(models.Model):
    title = models.CharField(max_length=50, blank=False, default="Unknown")

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class Instrument(models.Model):
    code = models.UUIDField(blank=False, default=uuid.uuid4, editable=True)
    brand = models.CharField(max_length=50, blank=False, default="Unknown")
    title = models.CharField(max_length=50, blank=False, default="Unknown")
    instrument_type = models.CharField(max_length=50, blank=True, default="")
    description = models.TextField(max_length=2000, null=True, blank=True)
    price = models.FloatField(
        blank=True,
        default=0.0,
        validators=[MinValueValidator(0.0), MaxValueValidator(100000.0)],
    )
    year_of_release = models.DateField(blank=True, null=True)
    genre = models.ManyToManyField(Genre, blank=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title
