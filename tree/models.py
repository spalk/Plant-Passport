import uuid
from django.db import models

# Create your models here.
class Branch(models.Model):
    unique_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return str(self.unique_id)
    