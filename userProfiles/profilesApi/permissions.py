# a class that DRF uses to determine if the user has a permission to make the change they're asking
# each time a request is made to our api, DRF checks if the request they're making is a legal request

from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """ Allow Users to update their own profile"""

    def has_object_permission(self, request, view, obj):
        """ Check if the user has permission to edit """
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id
