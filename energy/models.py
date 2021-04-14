from django.db import models


# Create your models here.
class Energy_generation(models.Model):

    def energy_default():
        return  {
        "jan": 0,
        "feb": 0,
        "mar": 0,
        "apr": 0,
        "may": 0,
        "jun": 0,
        "jul": 0,
        "aug": 0,
        "sep": 0,
        "oct": 0,
        "nov": 0,
        "dec": 0
      }

    power = models.FloatField()
    tilt = models.FloatField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    energy = models.JSONField("Energy", default = energy_default)
    average_energy = models.FloatField()
    year = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_date']
        verbose_name_plural = 'Energy'

    def __str__(self):
        return u'%s %s %s' % (self.power, self.latitude, self.longitude, self.tilt)

