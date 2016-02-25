import json

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db.models import F, Max, Q
from django.core.serializers.json import DjangoJSONEncoder

from rest_framework import viewsets

from .serializers import DeviceSerializer
from .models import Device

from Hydro.datapoint.serializers import DataPointSerializer
from Hydro.datapoint.forms import DataPointsCSVForm


class DeviceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class DeviceListView(ListView):
    model = Device

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            return super().get_queryset(*args, **kwargs).annotate(latest=Max(F('datapoint__collected_at')))\
                .filter(Q(owner=self.request.user) | Q(public=True))
        return super().get_queryset(*args, **kwargs).annotate(latest=Max(F('datapoint__collected_at')))\
            .filter(public=True)


class DeviceDetailView(DetailView):
    model = Device
    slug_field = "token"
    slug_url_kwarg = "token"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.object.datapoint_set.order_by('-collected_at')

        context['datapoints'] = json.dumps(DataPointSerializer(queryset.only('collected_at', 'data')[:1000],
                                                               many=True).data)
        context['form'] = DataPointsCSVForm()
        return context
