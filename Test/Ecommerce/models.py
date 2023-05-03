from django.db import models

# Create your models here.
class Cofee(models.Model):
    Name = models.TextField()
    image = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price  = models.IntegerField()