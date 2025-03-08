from django.db import models
from django.contrib.auth.models import User


def user_avatar_upload_path(instance, filename):
    """Generate file path for user avatars"""
    return f"avatars/{instance.id}/{filename}"


# class CustomUser(AbstractUser):
#     id = models.AutoField(primary_key=True)
#     nickname = models.CharField(max_length=32, blank=False, null=False, unique=True)
#     avatar = models.ImageField(upload_to=user_avatar_upload_path, blank=True, null=True)
#     desc = models.TextField(blank=True, null=True)
#     createdAt = models.DateTimeField(auto_now_add=True)
#     lastLoginAt = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return f"nickname: {self.nickname}, email: {self.email}"


class Collection(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=False, null=False)
    desc = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    modifiedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "title: {}, desc: {}".format(self.title, self.desc)


class CollectionImage(models.Model):
    id = models.AutoField(primary_key=True)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    path = models.TextField(blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    modifiedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "path: {}".format(self.path)
