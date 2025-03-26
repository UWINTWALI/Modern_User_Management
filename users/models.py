from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def save(self, *args, **kwargs):
        self.name = self.name.lower()  # Store in lowercase to enforce uniqueness
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name.capitalize()  # Display with first letter uppercase


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True, default='profile_pics/default_profile.png')
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    # def get_profile_picture(self):
    #     if self.profile_picture:
    #         return self.profile_picture.url
    #     return "/media/profile_pics/default_profile.png"
