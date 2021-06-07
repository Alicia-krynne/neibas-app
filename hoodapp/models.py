from django.db import models
from django.contrib.auth.models import User
import cloudinary
from cloudinary.models import CloudinaryField

# Create your models here.

class Hood(models.Model):
    name = models.CharField(max_length =30,null=True)
    location = models.CharField(max_length =30,null=True)
    image = CloudinaryField("media")
    occupants = models.IntegerField(null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    objects = models.Manager()
    # Admin Foreign key
    def __str__(self):
        return self.name


    def save_hood(self):
        self.save()

    def delete_hood(self):
        self.delete()


    @classmethod
    def delete_hood_by_id(cls, id):
        hood = cls.objects.filter(pk=id)
        hood.delete()

    @classmethod
    def get_hood_by_id(cls, id):
        hood = cls.objects.get(pk=id)
        return hood

    @classmethod
    def filter_by_location(cls, location):
        hood = cls.objects.filter(location=location)
        return hood

    @classmethod
    def search_hood(cls, search_term):
        hood= cls.objects.filter(neighbourhood_name__icontains=search_term)
        return hood

    @classmethod
    def update_hood(cls, id):
        hood= cls.objects.filter(id=id).update(id=id)
        return hood

   


# User class
class Profile(models.Model):
    pro_photo = CloudinaryField("media")
    name = models.CharField(max_length =30,null=True)
    location = models.CharField(max_length =30,null=True)
    email = models.EmailField(max_length =50,null=True)
    neighbourhood = models.ForeignKey(Hood, on_delete=models.CASCADE)
    bio = models.CharField(max_length =150,default='WELCOME TO  HOODAPP')
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile',null=True)
    
    def __str__(self):
        return self.name

    def save_profile(self):
        self.save()
        

    def delete_profile(self):
        self.delete()


class Business(models.Model):
    name = models.CharField(max_length =30,null=True)
    description = models.CharField(max_length =130,null=True)
    email = models.EmailField(max_length =50,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(Hood, on_delete=models.CASCADE)
 
    objects = models.Manager()
    def __str__(self):
        return self.name

    def save_biz(self):
        self.save()

    def delete_biz(self):
        self.delete()


    @classmethod
    def delete_business_by_id(cls, id):
        businesse = cls.objects.filter(pk=id)
        businesse.delete()

    @classmethod
    def get_business_by_id(cls, id):
        business = cls.objects.get(pk=id)
        return business

    @classmethod
    def filter_by_location(cls, location):
        business = cls.objects.filter(location=location)
        return business

  

    @classmethod
    def update_business(cls, id):
        business = cls.objects.filter(id=id).update(id=id)
        return business

    @classmethod
    def update_business(cls, id):
        business = cls.objects.filter(id=id).update(id=id)
        return business

class Post(models.Model):
    post = models.CharField(max_length =130,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    neighbourhood = models.ForeignKey(Hood,on_delete=models.CASCADE,related_name='post',null=True)

    class Meta:
        ordering = ['id']
    objects = models.Manager()
 
    def __str__(self):
        return self.post

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()
