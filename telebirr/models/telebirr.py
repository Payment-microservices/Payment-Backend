from django.db import models
from general.models.created_modified import CreatedModified
from platforms.models.platforms import Platforms
# Create your models here.

class TelebirrRequest(CreatedModified):
    ACTION_TYPE = [
        ('pending','pending'),
        ('success','success'),
        ('failed','failed')
    ]
    platforms = models.ForeignKey(Platforms,related_name='platforms')
    appId = models.CharField(max_length=10)
    nonce = models.CharField(max_length=30)
    notify_Url = models.CharField(max_length=200)
    out_TradeNo = models.CharField(max_length=30)
    receive_Name = models.CharField(max_length=20)
    return_Url = models.CharField(max_length=200)
    short_Code = models.CharField(max_length=10)
    subject = models.CharField(max_length=20)
    timeout_Express = models.IntegerField(default=30)
    timestamp = models.CharField(max_length=15)
    total_Amount = models.IntegerField(default=1)
    item_type = models.CharField(max_length=30)
    status = models.CharField(choices=ACTION_TYPE,default='pending')
    