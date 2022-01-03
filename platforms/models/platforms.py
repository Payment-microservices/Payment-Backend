from django.db import models
from general.models.created_modified import CreatedModified
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Platforms(CreatedModified):
    user = models.ForeignKey(User, related_name='platforms')
    appKey = models.CharField(max_length=10)
    name = models.CharField(max_length=15)
    description = models.CharField(max_length=40)
    
