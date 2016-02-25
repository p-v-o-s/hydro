from __future__ import unicode_literals

from django.conf.urls import url


from .views import DeviceDetailView, DeviceListView


urlpatterns = [
    url(r'^$', DeviceListView.as_view(), name="list"),
    url(r'^device/(?P<token>[A-Za-z0-9-]+)$', DeviceDetailView.as_view(), name="detail")
]
