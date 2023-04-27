from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100,null=False,blank=False)

    def __str__(self):
        return self.name
    


class Article(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL,blank=True)
    description = models.TextField()
    
    image = models.ImageField(null=True,blank=True, upload_to='images')
    
  
       

    def __str__(self):
        return self.title       