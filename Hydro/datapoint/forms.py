from django import forms
from django.forms import Form, ModelForm
from .models import DataPoint, Point


class PointForm(ModelForm):

    class Meta:
        model = Point
        fields = ["_lat", "_lng", ]


class DataPointForm(ModelForm):

    class Meta:
        model = DataPoint
        fields = ['collected_at', 'data', 'type', 'extra', 'location']


class DataPointsCSVForm(Form):
    csv_file = forms.FileField(required=True, max_length=300)



"""
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    location = models.ForeignKey(Point, on_delete=models.CASCADE, null=True)
    added_at = models.DateTimeField(_("Added at"), auto_now_add=True)
    collected_at = models.DateTimeField(_("Collected at"))
    data = models.IntegerField(_("Data"))
    type = models.CharField(_("Type"), max_length=50, blank=True)
    extra = models.TextField(_("Extra"), blank=True)
"""
