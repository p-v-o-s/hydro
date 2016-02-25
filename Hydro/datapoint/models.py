from django.db import models
from django.utils.translation import gettext_lazy as _
from Hydro.device.models import Device


class Point(models.Model):
    _lat = models.DecimalField(_("Latitude"), max_digits=12, decimal_places=9)
    _lng = models.DecimalField(_("Longitude"), max_digits=12, decimal_places=9)

    def __str__(self):
        return "{},{}".format(self._lat, self._lng)


class DataPoint(models.Model):

    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    location = models.ForeignKey(Point, on_delete=models.CASCADE, null=True)
    added_at = models.DateTimeField(_("Added at"), auto_now_add=True)
    collected_at = models.DateTimeField(_("Collected at"))
    data = models.IntegerField(_("Data"))
    type = models.CharField(_("Type"), max_length=50, blank=True)
    extra = models.TextField(_("Extra"), blank=True)

    def get_absolute_url(self):
        pass

    def __str__(self):
        return "{} ==> {}".format(self.type, self.data)

    @property
    def owner(self):
        return self.device.owner
