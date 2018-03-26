import hashlib
from django.db import models


# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=200,blank=True,null=True)
    email = models.EmailField(max_length=200,blank=True,null=True)
    message = models.TextField(blank=True,null=True)

    def __str__(self):
        return "%s - %s" % (self.name,self.email)