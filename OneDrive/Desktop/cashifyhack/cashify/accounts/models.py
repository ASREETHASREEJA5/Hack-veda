from django.db import models

class MobileDevice(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='mobile_devices')

    def __str__(self):
        return f"{self.brand} {self.model}"
