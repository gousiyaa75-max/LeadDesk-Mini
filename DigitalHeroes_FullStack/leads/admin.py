from django.contrib import admin

from .models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    """Custom admin configuration for managing incoming leads."""

    list_display = ("name", "email", "budget", "status", "created_at")
    list_filter = ("status", "budget", "created_at")
    search_fields = ("name", "email")
    ordering = ("-created_at",)
    list_per_page = 20
