from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class UserProfile(models.Model):

    
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE,related_name='profile')
    profile_pic =models.ImageField(default='profile_pics/default.jpg',upload_to="profile_pics")
    name = models.CharField(max_length=100, blank=True,unique = False)
    title = models.CharField(max_length=200, blank=True)
    public_email = models.EmailField(max_length=254,blank =True,unique=False)
    bio = models.TextField( blank=True,null=True)
    location = models.CharField(max_length=200, blank=True)
    website = models.URLField(max_length=200,blank=True)
    company = models.CharField(max_length=100, blank=True)


    def __str__(self):
        return str(self.user)

    def get_object (self):
        return self.request.user

   
    def save(self, *args, **kwargs):
        super(UserProfile, self).save(*args, **kwargs)
        
        img=Image.open(self.profile_pic.path)

        if img.height > 200 or img.width >200:
            output_size=(200,200)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)


