from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    image = models.FileField(upload_to='products/')
    
    def __str__(self):
        return self.title
