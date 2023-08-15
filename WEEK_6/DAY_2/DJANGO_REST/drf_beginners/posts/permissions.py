from rest_framework import permissions


class IsAuthenticatedAndAdmin(permissions.Basepermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'POST']:
            return request.user.is_authenticated  #returns True - has permission
        # elif request.methow in ['PUT', 'DELETE']:
        #     if request.user.is_authenticated:
        #         return request.user.is_staff   #returns True - is admin/moderator
            
    def has_object_permission(self, request, view, obj):
        if request.methow in ['PUT', 'DELETE']:
             return obj.author == request.user 
    #check that the current logged in user is the author of the post
        
        
               
#has permission - it's all about the user and when we use it
#has object permission - only authentication allowed to the the specific object like author and his post