from django.contrib import admin
from . import models

import django.db.models

# Register your models here.

for k, v in models.__dict__.items():
    if isinstance(v, type) and issubclass(v, django.db.models.Model):
        admin.site.register(v)
