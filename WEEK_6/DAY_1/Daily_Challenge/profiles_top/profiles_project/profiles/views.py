from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Profile
# Create your views here.


@csrf_exempt
def create_profile(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        if name and email:
            profile = Profile(name=name, email=email)
            profile.save()
            return JsonResponse({"success":True, 'message':"profile created successfully"})
        else: 
            return JsonResponse({"success":False, "message" : "Invalid"})
        
        
@csrf_exempt
def delete_profile(request, profile_id):
    if request.method == 'DELETE':
        profile = get_object_or_404(Profile, id=profile_id)
        profile.delete()
        return JsonResponse({'success': True, 'message': 'Profile deleted successfully'})

#raises ValueError in the browser, don't know what's the issue, I guess smth with POST connection
