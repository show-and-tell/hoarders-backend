from django.contrib.auth.models import User
from hoarders.models import Collection, CollectionImage
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ["id", "title", "desc", "user", "createdAt", "modifiedAt"]


class CollectionImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectionImage
        fields = ["id", "collection", "user", "path", "createdAt", "modifiedAt"]
