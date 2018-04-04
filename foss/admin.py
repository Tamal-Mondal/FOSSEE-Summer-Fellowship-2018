from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.user)
admin.site.register(models.foss)
admin.site.register(models.tutorial_detail)
admin.site.register(models.payment)
