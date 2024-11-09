
from datetime import timezone
from django.db import models
# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    # You can add other fields like password, role, etc. based on your requirements
    password = models.CharField(max_length=100)  # For simplicity; you can use Django's auth system if you plan on adding authentication
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Optional phone number field
    notification_preference = models.CharField(
        max_length=50,
        choices=[('email', 'Email'), ('sms', 'SMS'), ('push', 'Push Notification')],
        default='email'
    )
    # To handle the user's emergency contacts
    emergency_contacts = models.ManyToManyField('EmergencyContact', related_name='users', blank=True)

    def __str__(self):
        return self.name
class EmergencyContact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='emergency_contacts')
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    relationship = models.CharField(max_length=50)  # Example: "Friend", "Family", etc.
    is_primary = models.BooleanField(default=False)  # Mark if the contact is a primary one

    def __str__(self):
        return f"{self.name} ({self.relationship})"


class Location(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='locations')  # One-to-Many
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    timestamp = models.DateTimeField(default=timezone.now)
