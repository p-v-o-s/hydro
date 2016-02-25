from rest_framework import serializers

from .models import DataPoint, Point
from Hydro.device.serializers import DeviceSerializer


class PointSerializer(serializers.ModelSerializer):

    class Meta:
        model = Point
        fields = ["_lat", "_lng"]


class DataPointSerializer(serializers.ModelSerializer):
    # device = DeviceSerializer(read_only=True)
    location = PointSerializer(read_only=True)

    class Meta:
        model = DataPoint
        fields = ['collected_at',
                  'data',
                  'type',
                  'location',
                  # 'added_at',
                  # 'extra',
                  # 'device',
                  ]
