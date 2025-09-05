from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    category_image = models.ImageField(upload_to="category/",null=True)
    slug = models.SlugField(unique=True)
    def __str__(self):
        return self.name
    

class Image(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='images')
    title = models.CharField(max_length=200)    
    description = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to='gallery/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title