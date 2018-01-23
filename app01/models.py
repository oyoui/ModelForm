from django.db import models

class Class_list(models.Model):
    name = models.CharField(max_length=32)

class User_info(models.Model):
    name = models.CharField(max_length=32)
    cid = models.ForeignKey("Class_list")