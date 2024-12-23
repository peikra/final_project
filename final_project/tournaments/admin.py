from django.contrib import admin
from tournaments.models import Tournament

# Register your models here.
@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "display_organizers",
        "display_teams",
        "start_date",
        "end_date",
        "stadium_place",
        "entry_fee",
        "teams_quantity",
    )
    search_fields = ("name",)

    def display_organizers(self, obj):
        return ", ".join(organizer.username for organizer in obj.organizers.all())

    def display_teams(self, obj):
        return ", ".join(team.name for team in obj.teams.all())

    display_organizers.short_description = "Organizers"
    display_teams.short_description = "Teams"