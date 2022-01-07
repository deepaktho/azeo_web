from django.db import models
# from django.contrib.auth.models import User
# Create your models here.

class Extendeduser(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    alternate_phone_number = models.CharField(max_length = 100)
    college =  models.CharField(max_length=100)
    current_year = models.IntegerField()
    permanent_address = models.TextField()
    state  = models.CharField(max_length=100)
    email = models.EmailField()
    pincode = models.IntegerField(null=True)
    # user = models.OneToOneField(User, on_delete= models.CASCADE)

class Azeo_id_user(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    alternate_phone_number = models.CharField(max_length = 100)
    college =  models.CharField(max_length=100)
    current_year = models.IntegerField()
    permanent_address = models.TextField()
    state  = models.CharField(max_length=100)
    email = models.EmailField()
    pincode = models.IntegerField(null=True)
    azeo_id = models.CharField(max_length=100,default=1)
    # user = models.OneToOneField(User, on_delete= models.CASCADE)

