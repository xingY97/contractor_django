from django.db import models
from django.contrib.auth.models import User
class Entry(models.Model):
    entry_title = models.CharField(max_length=50)
    entry_text = models.TextField()
    entry_date = models.DateTimeField(auto_now_add=True)
    entry_author = models.ForeignKey(User, on_delete=Models.CASCADE)

    class Meta:
        verbose_name_plural = "Entries"
