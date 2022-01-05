from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
from taggit.managers import  TaggableManager
from ckeditor.fields import RichTextField
from django.db.models.signals import pre_save
from blog.utils import unique_slug_generator



   


class Category (models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Article (models.Model):

    class PublishedManager (models.Manager):
        def get_queryset (self):
            return super().get_queryset().filter(status='published')


    options = (
            ('draft','Draft'),
            ('published' ,'Published')
        )


    author =models.ForeignKey (User,on_delete=models.CASCADE)
    list_header_image =models.ImageField(null=True,blank=True)
    detail_header_image = models.ImageField(null=True, blank=True,upload_to="images/")
    title =models.CharField(max_length=100)
    slug =models.SlugField(max_length=250,null=True, blank=True,)
    snippet =models.CharField(max_length=70,blank=True)
    reading_min = models.CharField(max_length=200, blank=True)
    content =RichTextField(blank=True,null=True)
    article_date=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=100,choices=options,default='draft')
    category = models.ForeignKey(Category, on_delete=models.PROTECT,default=1)
    objects=models.Manager()
    published_manager =PublishedManager()
    tag=TaggableManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering =('-article_date',)


    def snip (self):
        return self.snippet[:150]

    def get_absolute_url  (self):
        return  f"/articles/{self.slug}"

#generates a slug automatically if slug field is blank
def slug_generator (sender,instance,*arg,**kwargs):
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)

pre_save.connect(slug_generator,sender=Article)

class Comment (models.Model):
    post=models.ForeignKey (Article,related_name='comments',on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    content = models.TextField()
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title,self.name)

