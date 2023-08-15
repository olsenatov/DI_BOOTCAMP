from django.shortcuts import render
from .serializers import PostSerializer
from django.views.decorators.csrf import csrf_exempt #decorator for testing purposes
from .models import Post
from django.http import JsonResponse
# from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly 
from .permissions import IsAuthenticatedAndAdmin                                        
# AllowAny,  access for anyone
# IsAuthenticated, for logged in
# IsAdminUser only admins

# Create your views here.

@csrf_exempt
#csrf TOKEN provides security to the data passing through the webpage
def post_view(request):
    if request.method == 'GET': 
        #request is a kind of bundle of information what's happening on webpage
        #GET - client tries to get data out of the website, send:
        posts = Post.objects.all() #all of the data(django)
        serializer = PostSerializer(posts, many=True) #translate all of the data into json format, 
                                           #many - multiple posts to translate
        return JsonResponse(serializer.data, safe=False) #pass all of the data (json) to the browser
                                            #dict (not specific safe=)/ orderedDict (safe=False)
                                            
    if request.method == 'POST':
        # data = JSONParser.parse(request.response) #dict with data from the POST request -> change it into JSONParser
        # print('Data After Parsing', data)
        serializer = PostSerializer(data=request.POST)
        # print(serializer)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return JsonResponse({'error' : 'Invalid'})
        
#PUT - update
  #if request.method == 'PUT'
#   ...
#DELETE - 
 #if request.method == 'DELETE'
#  ...



class PostView(APIView):
    
    permission_classes = (IsAuthenticatedAndAdmin,)
    
    def get(self, request, *args, **kwargs ):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs ):
        serializer = PostSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)  #show the errors of the serializer
        
    def put(self, request, pk, *args, **kwargs ):  #pk - primary key identifier of what we're updating (instance)
        post = Post.objects.get(id=pk)
        serializer = PostSerializer(instance=post,data=request.data)
        #applying changes from request.data to the instance(post)
        if serializer.is_valid():
            serializer.save() #update the instance
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, request, pk, *args, **kwargs ):
       post = Post.objects.get(id=pk)
       post.delete()
       return Response({'message': f"The post {pk} has been deleted"})
    