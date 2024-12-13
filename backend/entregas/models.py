from django.db import models
from django.conf import settings  # Import settings

class Delivery(models.Model):
    address = models.CharField(max_length=255)
    responsible = models.CharField(max_length=100)
    observation = models.TextField(blank=True, null=True)
    driver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Update here
    delivery_date = models.DateField()
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Delivery to {self.address} by {self.driver.username} on {self.delivery_date}"