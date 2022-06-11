from urllib import request
from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User


class url(models.Model):
    link = models.CharField(max_length=1000)
    uid = models.CharField(max_length=10)
