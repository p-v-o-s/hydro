import uuid
from django.test import TestCase

from django.db import IntegrityError, transaction

from Hydro.users.models import User
from .models import Device


# Create your tests here.
class TestDB(TestCase):

    def setUp(self):
        User.objects.create(username='testuser')

    def test_create_device(self):
        device = Device()

        with transaction.atomic():
            with self.assertRaises(IntegrityError):
                device.save()

        user = User.objects.get(username='testuser')
        device.owner = user
        device.save()

        self.assertRegex(str(device.token), '[a-z0-9-]+')

    def test_dub_tokens(self):
        u = uuid.uuid4()
        d1 = Device(token=u, owner=User.objects.get(username='testuser'))
        d1.save()
        with self.assertRaises(IntegrityError):
            d2 = Device(token=u, owner=User.objects.get(username='testuser'))
            d2.save()
x
