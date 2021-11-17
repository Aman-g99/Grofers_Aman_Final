from django.contrib import admin
from django.db import models


class Store(models.Model):
    
    key = models.CharField(blank=False, max_length=1000, unique=True)
    value = models.CharField(max_length=1000)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id) + " : " + self.key


admin.site.register(Store)