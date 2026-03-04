from rest_framework.permissions import BasePermission


class IsAdminUserOnly(BasePermission):
    """
    관리자만 접근 가능하도록 제한
    """

    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_authenticated and
            request.user.is_staff
        )