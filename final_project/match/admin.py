from django.contrib import admin

from .models import MatchInvitation

@admin.register(MatchInvitation)
class MatchInvitationAdmin(admin.ModelAdmin):
    list_display = ("from_team", "to_team", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("from_team__name", "to_team__name")
    ordering = ("-created_at",)
    date_hierarchy = "created_at"

    def from_team(self, obj):
        return obj.from_team.name
    from_team.short_description = "From Team"

    def to_team(self, obj):
        return obj.to_team.name
    to_team.short_description = "To Team"