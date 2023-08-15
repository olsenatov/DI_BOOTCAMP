from rest_framework import permissions
from rest_framework.permissions import BasePermission
from .models import Department



class IsDepartmentAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        if isinstance(obj, Department) and obj.admin == request.user:
            return True

        return False
        