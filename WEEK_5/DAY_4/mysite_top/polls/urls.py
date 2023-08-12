from django.urls import path, include
from .views import index, post, about, all_post

urlpatterns = [
 
    path('index/', index, name='index'),
    path('post/<int:post_id>/', post, name='post'),
    path('about/', about, name='about'),
    path('author-posts/<str:author_name>', all_post, name='all authors posts')
]