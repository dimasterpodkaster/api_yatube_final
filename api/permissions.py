from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user == view.request.user

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
