from django.db import models

# Create your models here.
class UrlDetails(models.Model):
    # id = models.IntegerField
    long_url = models.URLField("URL", max_length=256, default='http://www.google.com', unique=True)
    short_url =  models.CharField(max_length=256)
    number_hits = models.IntegerField(default=0)
    number_hourly_hits = models.IntegerField(default=0)
    time = models.TimeField(auto_now=True)