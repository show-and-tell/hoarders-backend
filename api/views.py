from django.contrib.auth.models import User
from rest_framework import permissions, viewsets
from hoarders.models import Collection, CollectionImage
from .serializers import CollectionSerializer, CollectionImageSerializer

from api.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = []


class CollectionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows collections to be viewed or edited.
    """

    queryset = Collection.objects.all().order_by("-createdAt")
    serializer_class = CollectionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CollectionImageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows collections to be viewed or edited.
    """

    queryset = CollectionImage.objects.all().order_by("-createdAt")
    serializer_class = CollectionImageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
