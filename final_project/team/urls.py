from django.urls import path, include
from rest_framework.routers import DefaultRouter
from team.views import  CreateTeamViewSet
from .views import UpdateTeamWinsView, UpdateTeamDrawsView, UpdateTeamLosesView, UserTeamView, AddTeamMemberView, \
    RemoveTeamMemberView,TeamLeaderboardView,SearchTeamView

router = DefaultRouter()
router.register(r'teams', CreateTeamViewSet, basename='team')

urlpatterns = [
    path('', include(router.urls)),
    path('team/wins/<int:pk>/',UpdateTeamWinsView.as_view(),name="wins"),
    path('team/draws/<int:pk>/',UpdateTeamDrawsView.as_view(),name="draws"),
    path('team/loses/<int:pk>/',UpdateTeamLosesView.as_view(),name="loses"),
    path('myteam/',UserTeamView.as_view(),name='myteam'),
    path('add-member/', AddTeamMemberView.as_view(), name='add-team-member'),
    path('remove-member/', RemoveTeamMemberView.as_view(), name='remove-team-member'),
    path('leaderboard/',TeamLeaderboardView.as_view(),name='leaderboard'),
    path('search/team/',SearchTeamView.as_view(),name='search-team')


]