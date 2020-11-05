from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ("id", "email", "first_name", "last_name")
    list_display = (
        "id",
        "first_name",
        "last_name",
        "is_active",
        "email",
        "date_joined",
    )
