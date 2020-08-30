from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from apps.posts.serializes import PostSerializer
from apps.posts.services import PostService


class PostReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    """
        list:
        Возвращает список постов.

        Права доступа: Любой.

        retrieve:
        Возвращает один объект поста id

        Права доступа: Любой.
    """
    permission_classes = (AllowAny,)
    serializer_class = PostSerializer
    queryset = PostService.get_all()
