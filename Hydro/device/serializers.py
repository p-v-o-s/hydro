from django.core.urlresolvers import reverse
from rest_framework import serializers

from .models import Device


class DeviceSerializer(serializers.ModelSerializer):
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    added_at = models.DateTimeField(auto_now_add=True)
    token = models.UUIDField(default=uuid.uuid4, editable=False)
    """
    owner = serializers.CharField(max_length=200, read_only=True)
    token = serializers.UUIDField(read_only=True)
    added_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Device
        fields = ['owner',
                  'name',
                  'added_at',
                  'token',
                  'public',
                  ]
