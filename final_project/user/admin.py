from django.contrib import admin
from user.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "team_name", "is_staff", "is_active")
    list_filter = ("is_staff", "is_superuser", "is_active", "team")
    search_fields = ("username", "email", "team__name")
    ordering = ("username", "email")

    def team_name(self, obj):
        return obj.team.name if obj.team else "No Team"
    team_name.short_description = "Team"