# blogs/context_processors.py
from .models import Blog

def first_blog_url(request):
    # Fetch the blog URL (adjust the title filter as needed)
    blog = Blog.objects.filter(title="Welcome to our Blogs!").live().first()
    return {
        'first_blog_url': blog.url if blog else None,
    }