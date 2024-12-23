from django.contrib import admin
from .models import Chat


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ("match_invitation", "sender", "message_excerpt", "timestamp")
    list_filter = ("timestamp",)
    search_fields = ("sender__username", "message", "match_invitation__from_team__name", "match_invitation__to_team__name")
    ordering = ("-timestamp",)
    date_hierarchy = "timestamp"

    def message_excerpt(self, obj):
        return obj.message[:50] + "..." if len(obj.message) > 50 else obj.message
    message_excerpt.short_description = "Message"