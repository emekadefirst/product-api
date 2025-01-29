from .models import User
from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user.is_authenticated and request.user.role == User.ROLE.ADMIN
        )


class IsCouncellor(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user.is_authenticated and request.user.role == User.ROLE.COUNCELLOR
        )


class IsFaculty(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user.is_authenticated
            and request.user.role == User.ROLE.FACULTY

        )


class IsAccountant(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user.is_authenticated
            and request.user.role == User.ROLE.ACCOUNTANT
        )


class IsExaminer(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user.is_authenticated
            and request.user.role == User.ROLE.EXAMINER
        )


class IsExaminerOrAdmin(BasePermission):
    """
    Allows access only to users with the role of Examiner or Admin.
    """

    def has_permission(self, request, view):
        return bool(
            request.user.is_authenticated
            and request.user.role in [User.ROLE.EXAMINER, User.ROLE.ADMIN]
        )


class IsAccountantOrAdmin(BasePermission):
    """
    Allows access only to users with the role of Accountant or Admin.
    """
    def has_permission(self, request, view):
        return bool(
            request.user.is_authenticated
            and request.user.role in [User.ROLE.ACCOUNTANT, User.ROLE.ADMIN]
        )


class IsAdminOrCouncellor(BasePermission):
    """
    Allows access only to users with the role of Councellor or Admin.
    """

    def has_permission(self, request, view):
        return bool(
            request.user.is_authenticated
            and request.user.role in [User.ROLE.COUNCELLOR, User.ROLE.ADMIN]
        )
