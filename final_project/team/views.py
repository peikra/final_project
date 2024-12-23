from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, status, generics, filters
from rest_framework.exceptions import PermissionDenied, ValidationError
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from team.serializers import TeamSerializer
from team.models import Team
from .permissions import IsTeamOwner
from .serializer_utils import SerializerFactory
from .serializers import UpdateTeamSerializer, UpdateTeamWinsSerializer, UpdateTeamLosesSerializer, \
    UpdateTeamDrawsSerializer, UserTeamSerializer, UpdateTeamMembersSerializer
from user.models import User


@extend_schema(tags=["Team"])
class CreateTeamViewSet(viewsets.ModelViewSet):
    serializer_class = SerializerFactory(
        create=TeamSerializer,
        default=TeamSerializer,
        update=UpdateTeamSerializer
    )
    queryset = Team.objects.all()
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ("update", "destroy"):
            permission_classes = [IsAuthenticated, IsTeamOwner]
        elif self.action == "create":
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


@extend_schema(tags=['Wins'])
class UpdateTeamWinsView(generics.UpdateAPIView):
    queryset = Team.objects.all()
    serializer_class = UpdateTeamWinsSerializer
    permission_classes = [IsAuthenticated,IsTeamOwner]

    def get_object(self):
        team = super().get_object()

        if team.owner!=self.request.user:
            raise PermissionDenied("You Dont have a permission tu update")

        return team


@extend_schema(tags=['Draws'])
class UpdateTeamDrawsView(generics.UpdateAPIView):
    queryset = Team.objects.all()
    serializer_class = UpdateTeamDrawsSerializer
    permission_classes = [IsAuthenticated,IsTeamOwner]

    def get_object(self):
        team = super().get_object()

        if team.owner!=self.request.user:
            raise PermissionDenied("You Dont have a permission tu update")

        return team


@extend_schema(tags=['Loses'])
class UpdateTeamLosesView(generics.UpdateAPIView):
    queryset = Team.objects.all()
    serializer_class = UpdateTeamLosesSerializer
    permission_classes = [IsAuthenticated,IsTeamOwner]

    def get_object(self):
        team = super().get_object()

        if team.owner!=self.request.user:
            raise PermissionDenied("You Dont have a permission tu update")

        return team


@extend_schema(tags=['Myteam'])
class UserTeamView(ListAPIView):
    serializer_class = UserTeamSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Team.objects.filter(owner=self.request.user)


@extend_schema(tags=["Team"])
class AddTeamMemberView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UpdateTeamMembersSerializer

    def post(self, request, *args, **kwargs):
        try:
            team = Team.objects.get(owner=request.user)
            user_id = request.data.get('members')
            user = User.objects.get(pk=user_id[0])
            team.add_member(user)

            return Response(
                {"detail": f"User {user.username} added to the team successfully."},
                status=status.HTTP_200_OK
            )
        except Team.DoesNotExist:
            return Response(
                {"detail": "You do not have a team."},
                status=status.HTTP_400_BAD_REQUEST
            )
        except User.DoesNotExist:
            return Response(
                {"detail": "User not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        except ValidationError as e:
            return Response(
                {"detail": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

@extend_schema(tags=["Team"])
class RemoveTeamMemberView(generics.GenericAPIView):
    serializer_class = UpdateTeamMembersSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            team = Team.objects.get(owner=request.user)
            user_id = request.data.get('members')
            user = User.objects.get(pk=user_id[0])
            team.remove_member(user)

            return Response(
                {"detail": f"User {user.username} removed from the team successfully."},
                status=status.HTTP_200_OK
            )
        except Team.DoesNotExist:
            return Response(
                {"detail": "You do not have a team."},
                status=status.HTTP_400_BAD_REQUEST
            )
        except User.DoesNotExist:
            return Response(
                {"detail": "User not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        except ValidationError as e:
            return Response(
                {"detail": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )


@extend_schema(tags=["Leaderboard"])
class TeamLeaderboardView(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['wins']
    ordering = ['-wins']
    permission_classes = [AllowAny]


@extend_schema(tags=["Search"])
class SearchTeamView(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    permission_classes = [AllowAny]