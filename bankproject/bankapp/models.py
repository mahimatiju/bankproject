from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Detail(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField(max_length=100)
    address = models.TextField(max_length=250)
    district = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    account = models.CharField(max_length=100)
    material = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)
        verbose_name = 'detail'
        verbose_name_plural = 'details'

    def __str__(self):
        return '{}'.format(self.name)
