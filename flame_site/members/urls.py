from django.urls import path

from .views import index

app_name = 'members'

urlpatterns = [
    path('', index, name="index")
]
