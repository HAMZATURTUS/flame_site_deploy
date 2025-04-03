from django.contrib import admin
from django.db import models
from members.models import Member

# Create your models here.
class Category(models.Model): # forensics, crypto, web
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.name}"

class SubCategory(models.Model): # xor, aes, rsa
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.category.name} - {self.name}"
    
    class Meta:
        ordering = ['category__name', 'name'] # sorting

class Difficulty(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.name}"

class Writeup(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    difficulty = models.ForeignKey(Difficulty, on_delete=models.CASCADE, default=None)
    notion_link = models.CharField(max_length=200, default=None)
    author = models.ForeignKey(Member, on_delete=models.CASCADE, default=None)
    icon = models.ImageField(upload_to='icons/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.title}"