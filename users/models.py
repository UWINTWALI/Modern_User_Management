from django.db import models
from django.core.validators import RegexValidator
import os
from django.conf import settings


"""Model for Local User Location___________________________________________________________________________________"""
class UserLocation(models.Model):
    country = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    cell = models.CharField(max_length=100)
    village = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.village}, {self.cell}, {self.sector}, {self.district}, {self.province}, {self.country}"
    

"""Model for Foreigner User Location_________________________________________________________________________________"""
class ForeignerLocation(models.Model):
    """ e.g., "Anytown, CA 91234, USA """
    location = models.CharField(max_length=255)  

    def save(self, *args, **kwargs):      
        self.location = self.location.lower()
        super().save(*args, **kwargs)

    def __str__(self):       
        return self.location.capitalize()




"""User Model___________________________________________________________________________________________________________"""
def get_default_profile_pic():
    return os.path.join('profile_pics', 'default_profile.png')

class User(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    INTERSEX = 'I'

    SEX_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (INTERSEX, 'Intersex'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    userid = models.CharField(max_length=30)    
    sex = models.CharField(max_length=1,choices=SEX_CHOICES,default=MALE)
    phone = models.CharField(max_length=100,validators=[RegexValidator(regex=r'^\+?\d{9,15}$', message="Enter a valid phone number.")],unique=True)
    email = models.EmailField(unique=True)    
    profile_picture = models.ImageField(upload_to='profile_pics/',null=True, blank=True,default=get_default_profile_pic)

    # Location fields
    date_of_birth = models.DateField()
    location = models.ForeignKey(UserLocation, on_delete=models.CASCADE, null=True, blank=True)

    is_foreigner = models.BooleanField(default=False)
    foreign_location = models.CharField(max_length=255, null=True, blank=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

