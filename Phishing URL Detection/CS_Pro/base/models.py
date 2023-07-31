from django.conf import settings
from django.db import models

class log(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    activity_log = models.CharField(max_length=60)