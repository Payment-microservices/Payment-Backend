from django.db import models
from general.models.created_modified import CreatedModified
from .telebirr import TelebirrRequest

class TelebirrResponse(CreatedModified):
    request = models.OneToOneField(TelebirrRequest,on_delete=models.CASCADE)
    code = models.IntegerField(default=0)
    data = models.CharField(max_length=300)
    message = models.TextField(max_length=35)
    dateTime = models.CharField(max_length=20)
    path = models.CharField(max_length=200)
    errorDetails = models.CharField(max_length=200)
    extraData = models.CharField(max_length=100)