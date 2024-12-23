from rest_framework.routers import DefaultRouter
from tournaments.views import CreateTournamentViewSet
from django.urls import path, include
from tournaments.views import AddTeamOnTournamentView,LeaveTournamentView

router = DefaultRouter()
router.register(r'tournaments', CreateTournamentViewSet, basename='tournament')

urlpatterns = [
    path('', include(router.urls)),
    path('tournaments/<int:pk>/add_team/', AddTeamOnTournamentView.as_view(), name='add-team-to-tournament'),
    path('tournaments/<int:pk>/leave_tournament/', LeaveTournamentView.as_view(), name='leave-tournament'),

]