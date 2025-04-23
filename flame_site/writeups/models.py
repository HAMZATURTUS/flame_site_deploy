from django.contrib import admin
from django.db import models
from members.models import Member

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel
from wagtail.blocks import TextBlock, RichTextBlock

from wagtail.search import index

from wagtailcodeblock.blocks import CodeBlock
from wagtail.admin.panels import FieldPanel

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
    
class RootPage(Page):
    subpage_types = ['writeups.WriteupRootPage']
    parent_page_types = ['wagtailcore.page']
    show_in_menus_default = False


    class Meta:
        verbose_name = "Container for basically everything"

class WriteupRootPage(Page):
    subpage_types = ['writeups.Writeup']
    parent_page_types = ['wagtailcore.page', 'writeups.RootPage']
    show_in_menus_default = False

    

    class Meta:
        verbose_name = "Writeups Container"

class Writeup(Page):
    template = "writeups/writeup.html"
    
    subcategory = models.ForeignKey(SubCategory, on_delete=models.PROTECT)
    difficulty = models.ForeignKey(Difficulty, on_delete=models.PROTECT)
    author = models.ManyToManyField(
        Member,
        related_name='writeups',
        blank=False, 
        help_text="Ctrl + Click to select more than one author"
    )
    #icon = models.ImageField(upload_to='icons/', blank=True, null=True)
    
    body = StreamField([
        ("heading", RichTextBlock()),
        ("code", CodeBlock(label='Code')),
    ],

    blank=True,
    help_text = "Note to writers: Keep in mind that any reader of this writeup is most likely not coming from a CTF, but from a social media platform where a link to our website was shared. The reader does not have access to the source, so you must show as much information as possible using images and code. Make the reader feel like hes there solving the challenge with you and try to make sources that the reader can try to solve on his own"
    )

    content_panels = Page.content_panels + [
        FieldPanel("subcategory"),
        FieldPanel("difficulty"),
        FieldPanel("author"),
        FieldPanel("body"),
    ]
    
    parent_page_types = ['writeups.WriteupRootPage'] 
    subpage_types = [] 
    
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        
        # Add authors to context
        context['authors'] = self.author.all()
        context['difficulty'] = self.difficulty
        context['subcategory'] = self.subcategory.name
        
        
        return context
    
    def __str__(self):
        return self.title