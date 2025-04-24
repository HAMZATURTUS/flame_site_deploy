from django.db import models
from django.utils import timezone

from members.models import Member
from writeups.models import RootPage

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel
from wagtail.blocks import TextBlock, RichTextBlock

from wagtail.search import index

from wagtailcodeblock.blocks import CodeBlock
from wagtail.admin.panels import FieldPanel

# Create your models here.
class BlogType(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.name}"

class BlogRootPage(Page):
    subpage_types = ['blogs.Blog']
    parent_page_types = ['writeups.RootPage']
    show_in_menus_default = False

    

    class Meta:
        verbose_name = "Blogs Container"

class Blog(Page):
    template = "blogs/blog.html"
    
    date = models.DateTimeField(
        verbose_name="Post date",
        default=timezone.now,
        help_text="Date and time the article is published",
    )
    
    blog_type = models.ForeignKey(BlogType, on_delete=models.PROTECT, null=True, blank=True)
    author = models.ManyToManyField(
        Member,
        related_name='blogs',
        blank=False, 
        help_text="Ctrl + Click to select more than one author"
    )
    
    body = StreamField([
        ("heading", RichTextBlock()),
        ("code", CodeBlock(label='Code')),
    ],

    blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("blog_type"),
        FieldPanel("date"),
        FieldPanel("author"),
        FieldPanel("body"),
    ]
    
    parent_page_types = ['blogs.BlogRootPage'] 
    subpage_types = ['blogs.BlogChildPage'] 
    
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        
        # Add authors to context
        context['authors'] = self.author.all()
        context['blog_type'] = self.blog_type
        
        
        return context
    
    @staticmethod
    def get_url_from_title(title):
        blog = Blog.objects.filter(title=title).live().first()
        return blog.url if blog else None
    
    class Meta:
        verbose_name = "Blog"
        ordering = ["-date"] 
    
    def __str__(self):
        return self.title

class BlogChildPage(Page):
    template = "blogs/blogchildpage.html"
    
    body = StreamField([
        ("heading", RichTextBlock()),
        ("code", CodeBlock(label='Code')),
    ],

    blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]
    
    parent_page_types = ['blogs.Blog'] 
    subpage_types = [] 
    
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        parent_blog = self.get_parent().specific  # Access the parent Blog instance
        context['parent_blog'] = parent_blog
        return context
    
    class Meta:
        verbose_name = "BlogChildPage"
    
    def __str__(self):
        return self.title