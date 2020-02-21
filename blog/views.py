from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView
)
from .models import Post
# from django.http import HttpResponse

# adding a blog home route
def home(request):
    """
    Handles traffic from the home page of the blog.
    It returns what we want the user to see when they're sent to this route.
    """
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'    # default template: <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    # overide the form valid method
    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    # overide the form valid method
    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)

    # function that validates user is the post author
    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True

        return False

# adding a blog about route
# option 1
# def about(request):
#    return HttpResponse("<h1>Blog About</h1>")

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
