from django.db import models

# Create your models here.

class Telebotdata(models.Model):
    chat_id = models.CharField('chat_id', max_length= 50)
    name = models.TextField('name')

    def __str__(self):
        return self.name

class Camer(models.Model):
    chat_id = models.CharField('chat_id', max_length= 50)
    name = models.TextField('name')

    def __str__(self):
        return self.name        
    
