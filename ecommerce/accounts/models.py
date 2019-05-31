from django.db import models

class GuestEmail(models.Model):
    email       = models.EmailField(max_length=254)
    active      = models.BooleanField(default=True)
    update      = models.TimeField(auto_now=True)
    timestamp   = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    
