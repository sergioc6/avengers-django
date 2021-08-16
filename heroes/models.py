from django.db import models

# Create your models here.
from django.db import models


class Hero(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField('date created')
    updated_at = models.DateTimeField('date updated')


class Villain(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField('date created')
    updated_at = models.DateTimeField('date updated')
