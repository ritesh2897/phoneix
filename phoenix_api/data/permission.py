from rest_framework.permissions import BasePermission
from rest_framework import permissions


class MyPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser or request.method =="GET":                      
            return True
        elif request.user.is_active and request.method in permissions.SAFE_METHODS:
           return True


# class AdminPermissions(BasePermission):

#     def has_permission(self, request, view):
#         if request.user.is_superuser or request.method =="GET":                      
#             return True

        
# class ReadOnly_User(BasePermission):

#     def has_permission(self, request, view):
#         if request.user.is_active and request.method in permissions.SAFE_METHODS:
#             return True
