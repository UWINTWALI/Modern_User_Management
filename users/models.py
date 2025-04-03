from django.db import models
from django.core.validators import RegexValidator
import os
from django.conf import settings

"""Model for Local User Location_____________________________________________________________________________________________"""
class UserLocation(models.Model):
    country = models.CharField(max_length=100, null=False, blank=False)
    province = models.CharField(max_length=100, null=False, blank=False)
    district = models.CharField(max_length=100, null=False, blank=False)
    sector = models.CharField(max_length=100, null=False, blank=False)
    cell = models.CharField(max_length=100, null=False, blank=False)
    village = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f"{self.village}, {self.cell}, {self.sector}, {self.district}, {self.province}, {self.country}"


class ForeignerLocation(models.Model):
    foreign_location = models.CharField(max_length=255, null=False, blank=False)  # e.g., "Anytown, CA 91234, USA"

    def save(self, *args, **kwargs):
        # CRITICAL FIX: Correct field name
        self.foreign_location = self.foreign_location.lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.foreign_location.capitalize()

def get_default_profile_pic():
    return 'profile_pics/default_profile.png'  # Ensure this file exists in media/profile_pics/

"""User Model___________________________________________________________________________________________"""
class User(models.Model):
    CUSTOM = 'C'
    MALE = 'M'
    FEMALE = 'F'
    INTERSEX = 'I'

    SEX_CHOICES = [
        (CUSTOM, '...'),
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (INTERSEX, 'Intersex'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    userid = models.CharField(max_length=30, unique=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, default=CUSTOM)
    phone = models.CharField(
        max_length=15,
        validators=[RegexValidator(regex=r'^\+?\d{9,13}$', message="Enter a valid phone number.")],
        unique=True
    )
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True, default=get_default_profile_pic)
    
    # Location fields
    location = models.ForeignKey(UserLocation, on_delete=models.CASCADE , null=True, blank=True)
    foreign_location = models.ForeignKey(ForeignerLocation, on_delete=models.CASCADE, null=True, blank=True)
    is_foreigner = models.BooleanField(default=False)

    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
