from django.db import models
import datetime
from django.contrib.auth import get_user_model


class entry(models.Model):
    entry = models.CharField(max_length=200)
    entry_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.entry
