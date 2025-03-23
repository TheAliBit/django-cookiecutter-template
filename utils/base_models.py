from django.db import models
from uuid import uuid4

class ID(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4, editable=False)

    class Meta:
        abstract = True

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True