from django.urls import path
# import views.py from current directory
from . import views

urlpatterns = [
    path('', views.home, name="blog-home"),
]
