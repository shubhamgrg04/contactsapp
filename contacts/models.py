from django.db import models
from django.db.models import UniqueConstraint

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=256, null=False)
    last_name = models.CharField(max_length=256, null=True)
    company_name = models.CharField(max_length=256, null=True)
    email = models.EmailField(max_length=256, null=True)
    phone = models.CharField(max_length=256, null=False)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['phone'], name="unique_phone_number")
        ]
