from django.db import models

from carts.models import Cart

# stored value is left: displayed value on the right capitalized
ORDER_STATUS_CHOICES = (
    ('created', 'Created'),
    ('paid', 'Paid'),
    ('shipped', 'Shipped'),
    ('refunded', 'Refunded'),
)
class Order(models.Model):
    order_id        = models.CharField(max_length=120, blank=True) # random, unique
    # billing_profile = ?
    # shipping address
    # billing address
    cart            = models.ForeignKey(Cart, on_delete=models.CASCADE)
    status          = models.CharField(max_length=120, default='created', choices=ORDER_STATUS_CHOICES)
    shipping_total  = models.DecimalField(default=5.99, max_digits=100, decimal_places=2)
    total           = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)

    def __str__(self):
        return self.order_id

# generate order_id
# generate order total 