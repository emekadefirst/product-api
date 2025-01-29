from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "email", "username", "is_staff", "is_active", "created_at"]
    list_filter = ["is_staff", "is_active"]
    search_fields = ["email", "username", "phone_number"]
    ordering = ["created_at"]
    readonly_fields = ["id", "created_at"]



admin.site.register(User, UserAdmin)
