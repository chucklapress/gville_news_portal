from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication

# Create your views here.
from portalapi.serializers import RSSfeedSerializer, PostNCourierSerializer

from app.models import HeadlineArticle, LocalArticle



class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user

class RSSfeedAPIView(generics.ListCreateAPIView):
    queryset = HeadlineArticle.objects.all()
    serializer_class = RSSfeedSerializer

    def get_queryset(self):
        return HeadlineArticle.objects.all()

class RSSfeedDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HeadlineArticle.objects.all()
    serializer_class = RSSfeedSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)

class PostNCourierAPIView(generics.ListCreateAPIView):
    queryset = LocalArticle.objects.all()
    serializer_class = PostNCourierSerializer

    def get_queryset(self):
        return LocalArticle.objects.all()

class PostNCourierDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LocalArticle.objects.all()
    serializer_class = PostNCourierSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)
