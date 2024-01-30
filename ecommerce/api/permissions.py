from rest_framework import permissions

class IsVendor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_vendor
    
class IsCustomer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_customer

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser