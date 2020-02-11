from django.shortcuts import render
from django.http import HttpResponse

# adding a blog home route
def home(request):
    """
    Handles traffic from the home page of the blog.
    It returns what we want the user to see when they're sent to this route.
    """
    return HttpResponse("<h1>Blog Home</h1>")

# adding a blog about route
def about(request):
    return HttpResponse("<h1>Blog About</h1>")
