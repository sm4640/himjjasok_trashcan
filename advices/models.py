from django.db import models

# Create your models here.

class advice_him(models.Model):
    content = models.TextField('내용')

class advice_jja(models.Model):
    content = models.TextField('내용')

class advice_sok(models.Model):
    content = models.TextField('내용')
