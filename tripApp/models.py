from django.db import models
from geoposition.fields import GeopositionField
from geoposition import Geoposition
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Resort(models.Model):
    RESORT_TYPE_CHOICES = (
        ('HIS', 'History'),
        ('VIW', 'View'),
        ('ACT', 'Activity'),
        ('CUL', 'Culter'),
    )
    SEASON_CHOICES = (
        ('SP', 'Spring'),
        ('SU', 'Summer'),
        ('AU', 'Autumn'),
        ('WI', 'Winter'),
    )
    resort_name = models.CharField(max_length=100)
    resort_type = models.CharField(max_length=3, choices=RESORT_TYPE_CHOICES)
    hour_estimate = models.FloatField(
        default=1,
        help_text="How many hours would this point of interest would take? (0.5, 3. etc)")
    good_season = models.CharField(max_length=2, choices=SEASON_CHOICES)
    ticket_price = models.FloatField(
        default=0,
        help_text="Unit in YUAN, could translate into other currency in frontend")
    rate_star = models.FloatField(
        default=5,
        validators = [MinValueValidator(0), MaxValueValidator(5)],
        help_text="Rate how much you recommend traveller to go, from 0 - 5, you could do 4.7 as well")
    city = models.CharField(max_length=100, default='null')
    country = models.CharField(max_length=100, default='null')
    position = GeopositionField()
    def __str__(self):
        return self.resort_name
