from django.db import models
from datetime import datetime
# Create your models here.

class Chat(models.Model):
    msg = models.TextField(blank=True)
    sent_time=models.DateTimeField(default=datetime.now , blank=True)
    username = models.CharField(max_length=200)

    class meta:
        ordering=('sent_time')
    
