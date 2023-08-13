from django.urls import path, include
from .views import index, post, about, all_post, category_posts

urlpatterns = [
 
    path('index/', index, name='index'),
    path('post/<int:post_id>/', post, name='post'),
    path('about/', about, name='about'),
    path('author-posts/<str:author_name>', all_post, name='all authors posts'),
    path('category-posts/<int:category_id>', category_posts, name='posts per category')
]