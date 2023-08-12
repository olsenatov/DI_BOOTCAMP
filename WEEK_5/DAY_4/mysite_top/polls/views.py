from django.shortcuts import render
from .models import Post, Author
from django.http import HttpResponse #renders text on the top of blank page

# Create your views here.

def index(request):#the user uses app and sends requests holding inside information (who is the user, which browser he uses etc)
    message = "Hello, this is my first page"
    return HttpResponse(message)

def post(request, post_id:int):
    data = {
        1: "This is the 1st post",
        
        2: "This is the 2nd post"
    }
    post = data.get(post_id, 'No such post')
    return HttpResponse(post)

def about(request):
    text = "This is the page telling more about this webpage\n <h1> Hello World </h1>"
   
    return HttpResponse(text)

def all_post(request, author_name:str):
    author_name = author_name.capitalize()
    try:
        author_name = Author.objects.get(name=author_name)
    # author_posts = Post.objects.filter(author=author_name)

        author_posts = author_name.post_set.all()
        
        content = ''
        for post in author_posts:
            content +=post.title + '\n'
        return HttpResponse(content)
    except Author.DoesNotExist:
        return HttpResponse("no such author")