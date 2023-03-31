from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.User)
admin.site.register(models.Room)
admin.site.register(models.Post)
admin.site.register(models.Message)
admin.site.register(models.Album)
admin.site.register(models.Following)
