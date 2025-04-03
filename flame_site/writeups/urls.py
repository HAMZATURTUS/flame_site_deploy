from django.urls import path

from .views import index, wlist

app_name = 'writeups'

urlpatterns = [
    path('', index, name="index"),
    path('wlist/<int:category_id>', wlist, name="wlist")
]
