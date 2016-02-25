from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.db import transaction

from rest_framework import viewsets
from rest_framework import permissions

from .serializers import DataPointSerializer
from .permissions import IsOwnerOrReadOnly
from .models import DataPoint
from .forms import DataPointsCSVForm

from Hydro.device.models import Device


class DataPointViewSet(viewsets.ModelViewSet):
    serializer_class = DataPointSerializer
    queryset = DataPoint.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)


# class BulkUploadFormView(FormView):
#     form_class = DataPointsCSVForm
#     template_name = 'bluk.html'
#     success_url = '/uploaded'
#
#     def form_valid(self, form):
#         for i in form:
#             print(i)
#         return super().form_valid(form)


def bulk_upload(request):
    if request.method == 'POST':
        form = DataPointsCSVForm(request.POST, request.FILES)
        if form.is_valid():
            # process the file
            with transaction.atomic():
                for i in request.FILES['csv_file']:
                    token, timestamp, data = i.decode().strip().split(',')
                    time = datetime.fromtimestamp(int(timestamp))
                    data = float(data)
                    device = get_object_or_404(Device, token=token)
                    if device.owner == request.user:
                        DataPoint(data=data, collected_at=time, device=device).save()
                return redirect(reverse('devices:detail', kwargs={"token": device.token}) or reverse('devices:list'))
    return redirect(reverse('devices:list'))
