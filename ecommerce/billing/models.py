from django.conf import settings
from django.db import models
from django.db.models.signals import post_save

User = settings.AUTH_USER_MODEL

# i want one user to have one biling profile when they sign up
# auto make billing profile when user is created
class BillingProfile(models.Model):
    user        = models.ForeignKey(User, null=True, blank=True)
    email       = models.EmailField(max_length=254)
    active      = models.BooleanField(default=True)
    update      = models.TimeField(auto_now=True)
    timestamp   = models.TimeField(auto_now_add=True)
    # I want to create customer_id for stripe or braintree here later

    def __str__(self):
        return self.email
        
# use signals to auto create billing profile on user creation         
def user_created_reciever(sender, instance, created, *args, **kwargs):
    if created:
        BillingProfile.objects.get_or_create(user=instance)

post_save.connect(user_created_reciever, sender=User)