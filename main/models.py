from django.db import models

# Create your models here.
class Message(models.Model):
    text = models.TextField()
    text_en = models.TextField(default="")
    text_de = models.TextField(default="")
    
