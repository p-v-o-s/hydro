from __future__ import unicode_literals

from django.conf.urls import url


from .views import DataPointViewSet, bulk_upload


urlpatterns = [
    url(r'^list/$', DataPointViewSet.as_view({'get': 'list',
                                              'post': 'create',
                                              }), name="list"),

    url(r'bulk/$', bulk_upload, name="bulk"),
    # url('^detail/(?P[])$'),
    # url(r'^$', ),
    # url(r'^device/(?P<token>[A-Za-z0-9-]+)$', DeviceDetailView.as_view(), name="detail")
]
