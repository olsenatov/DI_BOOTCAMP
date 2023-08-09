from django.shortcuts import render

from django.http import HttpResponse
from .data import animals, families

# Create your views here.
def display_all_animals(request):
    all_animals = []
    for animal in animals:
         formatted_animal = f"Name: {animal['name']}, Legs: {animal['legs']}, Weight: {animal['weight']}, Height: {animal['height']}, Speed: {animal['speed']} \n"
         all_animals.append(formatted_animal)
    return HttpResponse(all_animals)

def display_all_families(request):
    all_families = []
    for family in families:
        formatted_family = f"Family Name: {family['name']} \n"
        all_families.append(formatted_family)
    return HttpResponse(all_families)
        

def display_one_animal(request, animal_id):
    data = []
    for animal in animals:
        if animal_id == animal["id"]:
             data.append(f"Name: {animal['name']}, Legs: {animal['legs']}, Weight: {animal['weight']}, Height: {animal['height']}, Speed: {animal['speed']} \n")
        
    return HttpResponse(data) 

def display_animal_per_family(request, family_id):
    data = []
    for num in families:
        for animal in animals:
            if animal['family'] == num['id'] and num["id"] == family_id:
                data.append(f"Name: {animal['name']}, Legs: {animal['legs']}, Weight: {animal['weight']}, Height: {animal['height']}, Speed: {animal['speed']} \n")
    return HttpResponse(data) 