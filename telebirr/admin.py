from django.contrib import admin
from .models.telebirr import TelebirrRequest
from .models.response import TelebirrResponse
# Register your models here.

admin.site.register(TelebirrRequest)
admin.site.register(TelebirrResponse)