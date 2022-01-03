from django.db import models
from general.models.created_modified import CreatedModified
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
User = get_user_model()

# Create your models here.

def profile_path(instance, filename):
    return 'profile/{filename}'.format(filename=filename)

class Profiles(CreatedModified):
    user = models.ForeignKey(User, related_name='platforms')
    total_amount = models.FloatField(max_length=10000000,default=0,validators=[MinValueValidator(0)])
    avatar = models.ImageField(_('Image'),upload_to=profile_path)
    first_name = models.CharField(max_length=15, blank=True)
    last_name = models.CharField(max_length=15, blank=True)
    have_wallet = models.BooleanField(default=False)
    publickey = models.CharField(max_length=256,blank=True,null=True)
    appkey = models.CharField(max_length=30, blank=True,null=True)
    appid = models.CharField(max_length=30,blank=True,null=True)
    short = models.CharField(max_length=10, blank=True,null=True)
