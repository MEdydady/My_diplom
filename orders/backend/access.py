from rest_framework import permissions


class Owner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.user


class Shops(permissions.BasePermission):
    def has_permission(self, request, view):
        type = request.user.type
        return type == "shop"
