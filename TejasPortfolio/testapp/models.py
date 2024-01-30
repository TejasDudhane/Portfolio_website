from django.db import models
class ContactDb(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    message = models.TextField()
