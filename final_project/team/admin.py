from django.contrib import admin
from team.models import Team

# Register your models here.
@admin.register(Team)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "location",
        "owner",
        "wins",
        "losses",
        "draws",
        "logo"
    )
    search_fields = (
        "name",

    )