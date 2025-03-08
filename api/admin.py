from django.contrib import admin
from hoarders.models import Collection


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "user", "createdAt", "modifiedAt")
    search_fields = ("title", "desc", "user__username")
    list_filter = ("createdAt", "modifiedAt")
    ordering = ("-createdAt",)

    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user = request.user
        super().save_model(request, obj, form, change)
