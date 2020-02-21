from django.urls import path
# import views.py from current directory
from . views import (PostListView, 
    PostDetailView,
    PostCreateView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name="blog-home"),
    # int -> integers only; pk -> primary key
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('post/new/', PostCreateView.as_view(), name="post-create"),
    path('about/', views.about, name="blog-about"),
]
