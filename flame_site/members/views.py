from django.shortcuts import render
from django.http import HttpResponse

from .models import Member

# Create your views here.
def index(request):
    
    member_list = Member.objects.order_by("id")
    
    context = {"member_list": member_list}
    
    return render(request, "members/index.html", context)