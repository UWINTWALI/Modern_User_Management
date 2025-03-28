from django.db import models
from django.core.validators import RegexValidator
import os
from django.conf import settings


"""Model for Local User Location"""
class Country(models.Model):
    name = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        """Store name in lowercase"""
        self.name = self.name.lower() 
        super().save(*args, **kwargs)

    def __str__(self):
        """Display with the first letter uppercase"""
        return self.name.capitalize()  


class Province(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        self.name = self.name.lower() 
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name.capitalize() 


class District(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        self.name = self.name.lower() 
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name.capitalize() 


class Sector(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        self.name = self.name.lower()  
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name.capitalize() 


class Cell(models.Model):
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        self.name = self.name.lower()  
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name.capitalize() 

class Village(models.Model):
    cell = models.ForeignKey(Cell, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        self.name = self.name.lower() 
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name.capitalize() 

"""Model for Foreigner User Location"""
class ForeignerLocation(models.Model):
    """ e.g., "Anytown, CA 91234, USA """
    location = models.CharField(max_length=255)  

    def save(self, *args, **kwargs):      
        self.location = self.location.lower()
        super().save(*args, **kwargs)

    def __str__(self):       
        return self.location.capitalize()



# User Model
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
    is_foreigner = models.BooleanField(default=False)
    country = models.ForeignKey('Country', on_delete=models.SET_NULL, null=True, blank=True)
    province = models.ForeignKey('Province', on_delete=models.SET_NULL, null=True, blank=True)
    district = models.ForeignKey('District', on_delete=models.SET_NULL, null=True, blank=True)
    sector = models.ForeignKey('Sector', on_delete=models.SET_NULL, null=True, blank=True)
    cell = models.ForeignKey('Cell', on_delete=models.SET_NULL, null=True, blank=True)
    village = models.ForeignKey('Village', on_delete=models.SET_NULL, null=True, blank=True)
    foreign_location = models.CharField(max_length=255, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.is_foreigner:
            self.province = None
            self.district = None
            self.sector = None
            self.cell = None
            self.village = None
        else:
            self.foreign_location = None
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
