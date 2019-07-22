from django.db import models

# Create your models here.
class stock (models.Model):
    name = models.CharField(max_length=100)
    password1 = models.CharField(max_length=10)
    password2 = models.CharField(max_length=10)

    def __str__(self):
        return self.name