from django.db import models

### User model (assuming you have a custom user model or you can use Django's default User model)

```

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.username

```

### Location model with a foreign key to the User model

```
class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='locations')

    def __str__(self):
        return self.name
```









```

I have the following functionality in my CRUD operation:

User Model with the following attributes:


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

I want to add the location field on the user. there should be reference to the Location Model the contain the location of the user.
what I thought, the location field should allow the system to registration of the new location by typing and save it in database. if you want to save another user with the same location like in the database you will click on location as if you are going to type and view the existing one as if you are searching, if not present and is first time that location is specified, the system will allow you to type it and save it in the location table while saving the reference to that location in the users table. All tyipng new or selecting location or searching location done in single input field that is clean and minimalist on the front-end location field.

This is CRUD I'm doing in Django. but it has only: 
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
I want to add that location that allow to type in the same field as we search and select if not availabe.



```