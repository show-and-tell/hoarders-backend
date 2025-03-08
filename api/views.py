from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework import permissions, viewsets, status
from rest_framework.response import Response
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
    API endpoint that allows collection images to be viewed, edited, renamed via query parameters, or deleted.
    """

    queryset = CollectionImage.objects.all().order_by("-createdAt")
    serializer_class = CollectionImageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=["patch"])
    def rename(self, request):
        """
        Custom endpoint to rename a collection image using a query parameter.
        Example: PATCH /collectionimages/rename?path=image_name&new_name=new_image_name
        """
        path = request.query_params.get("path")

        if not path:
            return Response(
                {"error": "Both 'path' and 'new_name' parameters are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            collection_image = CollectionImage.objects.get(
                id=request.query_params("id"), user=request.user
            )
        except CollectionImage.DoesNotExist:
            return Response(
                {"error": "Image not found or you don't have permission"},
                status=status.HTTP_404_NOT_FOUND,
            )

        collection_image.path = path
        collection_image.save()

        return Response(
            {"message": "Name updated successfully", "path": path},
            status=status.HTTP_200_OK,
        )

    def destroy(self, request, *args, **kwargs):
        """
        Override DRF's default DELETE method to delete a collection image.
        """
        instance = CollectionImage.objects.get(id=request.query_params("id"))
        instance.delete()
        return Response(
            {"message": "Image deleted successfully"}, status=status.HTTP_204_NO_CONTENT
        )
