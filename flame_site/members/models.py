from django.db import models

# Create your models here.
class University(models.Model):
    name = models.CharField(max_length=50)
    initials = models.CharField(max_length=10)
    logo = models.ImageField(upload_to='uni_logos/', default='portraits/placeholder.png')
    
    def __str__(self):
        return f"{self.name}"

class Major(models.Model):
    name = models.CharField(max_length=50)
    initials = models.CharField(max_length=5)
    
    def __str__(self):
        return f"{self.name}"

class Member(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='portraits/', default='portraits/placeholder.png')
    university = models.ForeignKey(University, on_delete=models.CASCADE, null=True)
    major = models.ForeignKey(Major, on_delete=models.CASCADE, null=True)
    linkedin = models.CharField(max_length=100, null=True)
    github = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"