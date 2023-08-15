from rest_framework.permissions import permissions


class IsForecaster(permissions.Basepermission):
    def has_object_permission(self,  request, view, obj):
        if request.method == 'DELETE':
            return request.user == obj.forecaster
        
    
    
    
    # def has_permission(self, request, view):
    #     if request.method in ['GET', 'POST']:
    #         return request.user.is_authenticated  #returns True - has permission
    #     # elif request.methow in ['PUT', 'DELETE']:
    #     #     if request.user.is_authenticated:
    #     #         return request.user.is_staff   #returns True - is admin/moderator
            
    # def has_object_permission(self, request, view, obj):
    #     if request.methow in ['PUT', 'DELETE']:
    #          return obj.forecaster == request.user 