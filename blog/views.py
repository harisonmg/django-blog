from django.shortcuts import render
# from django.http import HttpResponse

posts = [
    {
        'author': 'Harison Mwangi',
        'title': 'Blog post 1',
        'content': 'First post content', 
        'date_posted': '12 February 2020',
    },

    {
        'author': 'Jane Doe',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': '13 February 2020',
    }

]

# adding a blog home route
def home(request):
    """
    Handles traffic from the home page of the blog.
    It returns what we want the user to see when they're sent to this route.
    """
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

# adding a blog about route
# option 1
# def about(request):
#    return HttpResponse("<h1>Blog About</h1>")

def about(request):
    return render(request, 'blog/about.html')
