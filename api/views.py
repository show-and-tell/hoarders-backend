import json
from django.contrib.auth.models import Group, User
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions, viewsets

from api.serializers import GroupSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all().order_by("name")
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


@csrf_exempt
def user_login(request):
        try:
            data = json.loads(request.body)  # 解析 JSON 数据
            username = data.get("username")
            password = data.get("password")
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        if not username or not password:
            return JsonResponse({"error": "bad request"}, status=400)

        user = authenticate(username=username, password=password)
        if user:
            # login(request, user)
            return JsonResponse({"message": "success", "username": user.username, "user_id": user.id})
        else:
            return JsonResponse({"error": "incorrect username or password"}, status=401)

        return JsonResponse({"error": "only post"}, status=405)
