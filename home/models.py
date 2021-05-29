from django.conf import settings
from django.db import models


class Patient(models.Model):
    "Generated Model"
    patientname = models.TextField(
        blank=True,
    )
    age = models.IntegerField(
        null=True,
        blank=True,
    )
    address = models.TextField(
        null=True,
        blank=True,
    )
    phonenumber = models.CharField(
        max_length=256,
        null=True,
        blank=True,
    )
    problem = models.TextField(
        null=True,
        blank=True,
    )
    o2level = models.IntegerField(
        null=True,
        blank=True,
    )
    doctor = models.TextField(
        null=True,
        blank=True,
    )
    problemsice = models.DateTimeField(
        null=True,
        blank=True,
    )
