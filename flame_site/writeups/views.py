from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Writeup, Category

# Create your views here.
def index(request):
    
    category_list = Category.objects.order_by('name')
    context = {"category_list": category_list}
    
    return render(request, "main_page/index.html", context)

def wlist(request, category_id):
    
    category = get_object_or_404(Category, id=category_id)
    
    writeup_list = Writeup.objects.filter(subcategory__category=category)
    
    easy_writeups = writeup_list.filter(difficulty__name='Easy')
    medium_writeups = writeup_list.filter(difficulty__name='Medium')
    hard_writeups = writeup_list.filter(difficulty__name='Hard')
    
    context = {
        'category': category,
        'easy_writeups': easy_writeups,
        'medium_writeups': medium_writeups,
        'hard_writeups': hard_writeups,
    }
    
    return render(request, "writeups_list/writeups.html", context)