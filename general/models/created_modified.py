from django.db import models
from django.utils import timezone


class CreatedModified(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, db_index=True, null=True)
    modified_date = models.DateTimeField(default=timezone.now, db_index=True)

    class Meta:
        abstract = True
