from rest_framework import viewsets
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404

from .serializers import FollowSerializer
from posts.models import Follow


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
