from django.db import models

# Create your models here.
from django.db import models


class Guest(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    nationality = models.CharField(max_length=50)
    id_number = models.CharField(max_length=50, verbose_name="Číslo dokladu")
    checkin_date = models.DateField()
    checkout_date = models.DateField()

    STAY_TYPE_CHOICES = [
        ('short', 'Krátkodobý'),
        ('long', 'Dlouhodobý'),
    ]
    stay_type = models.CharField(max_length=10, choices=STAY_TYPE_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
