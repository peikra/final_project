from django.urls import path
from user.views import RegisterView,RefreshTokenCustomView
from user.views import LoginView
from user.views import UserViewSet
from user.views import LeaveTeamView,SearchUserView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path("login/", LoginView.as_view(), name="login"),
    path("token/refresh/", RefreshTokenCustomView.as_view(), name="token_refresh"),
    path('userinfo/',UserViewSet.as_view(),name='user'),
    path('leave-team/', LeaveTeamView.as_view(), name='leave_team'),
    path('search/user/',SearchUserView.as_view(),name='search-user')

]
