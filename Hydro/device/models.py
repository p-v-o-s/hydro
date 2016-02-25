import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _

from Hydro.users.models import User


# Create your models here.
class Device(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(_("Name"), max_length=50)
    added_at = models.DateTimeField(_("Added at"), auto_now_add=True)
    token = models.UUIDField(_("Token"), default=uuid.uuid4, editable=False, unique=True)
    public = models.BooleanField(_("Public"), default=False)

    def __str__(self):
        return self.name
