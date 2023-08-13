from django.shortcuts import render
from .models import Book
from django.http import JsonResponse
from requests import request
# import json
# Create your views here.

def list_books(request):
    return JsonResponse(Book.objects.all())

#Yossi said 5.3 is not mandatory to create_book with POST

def book_detail(request, book_id:int):
    try:
        lib = Book.objects.get(book_id=id)
        book_data = {}
        for n in lib:
            book_data[book_id].apend(n)
        return JsonResponse(book_data)
    except Book.DoesNotExist:
        return JsonResponse({"error" : "Book not found"}, status=404)


#6. can't make it import different books, somehow populate.py imports the same book all the time

