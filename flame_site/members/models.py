from django.db import models

# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='portraits/', default='portraits/placeholder.png')
    linkedin_url = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"