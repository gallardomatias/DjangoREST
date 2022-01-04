from django.urls import path
from .views import PostsListView, PostDetailView

app_name="blog"

urlpatterns = [
    path('posts/', PostsListView.as_view()),
    path('posts/<post_slug>/', PostDetailView.as_view())
]