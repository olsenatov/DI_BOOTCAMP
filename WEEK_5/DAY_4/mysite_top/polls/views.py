from django.shortcuts import render
from .models import Post, Author, Category
from django.http import HttpResponse #renders text on the top of blank page

# Create your views here.

def index(request):#the user uses app and sends requests holding inside information (who is the user, which browser he uses etc)
    message = "Hello, this is my first page"
    return HttpResponse(message)

def post(request, post_id:int):
    try:
        post = Post.objects.get(id= post_id)
        content = f'Author {post.author.name} | Title: {post.title} | Title: {post.text}'
        
        return HttpResponse(post)
    
    except Post.DoesNotExist:
       return HttpResponse('No such post')
   

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
 
 #create a view that accepts id of a category and returns an HttpResponse with all the posts from that category   
def category_posts(requests, category_id:int):
    try:
        category = Category.objects.get(id=category_id)
        posts = category.posts.all()
        content = ''
        for post in posts:
          content += f'{post.title} - {post.author}'
        
        return HttpResponse(content)
    
    except Category.DoesNotExist:
       return HttpResponse('No such category')
    