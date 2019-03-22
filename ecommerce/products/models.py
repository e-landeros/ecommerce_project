from django.db import models
import random 
import os

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext 

def upload_image_path(instance, filename):
    print(instance)
    print(filename)
    new_filename = random.randint(1, 3910892383)
    name, ext = get_filename_ext(filename)
    final_filename = f'{new_filename}{ext}'
    return f'products/{new_filename}/{final_filename}'

class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    image = models.FileField(upload_to=upload_image_path, null=True, blank=True)

    def __str__(self):
        return self.title
