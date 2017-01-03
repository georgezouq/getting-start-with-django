from django.db import models

class TodoItem(models.Model):
    id = models.TextField(blank=False, null=False)
    text = models.TextField(blank=False, null=False)
    date_posted = models.DateField(auto_now=True)
