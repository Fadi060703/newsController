from django.db import models

# Create your models here.
class Article( models.Model ) :
    image = models.ImageField( upload_to = 'media/images/' ) 
    headline = models.CharField( max_length = 255 ) 
    text = models.TextField() 
    
