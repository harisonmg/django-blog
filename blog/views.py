from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    """
    Handles traffic from the home page of the blog.
    It returns what we want the user to see when they're sent to this route.
    """
    return HttpResponse("<h1>Blog Home</h1>")