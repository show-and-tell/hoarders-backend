from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=32, blank=False, null=False)
    avatar = models.TextField(max_length=512, blank=True, null=True)
    email = models.EmailField(unique=True)
    desc = models.TextField(blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    lastLoginAt = models.DateTimeField()

    def __str__(self):
        return "nickname: {}, email: {}".format(self.nickname, self.email)


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


