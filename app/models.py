from django.db import models

class coordenadasAgresor(models.Model):
    lat = models.CharField(max_length=50)
    lng = models.CharField(max_length=50)
    
    def __str__(self):
        return self
