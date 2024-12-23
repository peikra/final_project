from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.cache import cache_page
from drf_spectacular.utils import extend_schema
from rest_framework import status, generics, filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from user.serializers import UserSerializer,UserLoginSerializer
from user.models import User
from user.serializers import UserInfoSerializer


# Create your views here.
@extend_schema(tags=["Auth"])
class RegisterView(APIView):
    """
    View for users registration
    """

    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return Response({
                'message': 'Login successful',
                'user': UserSerializer(user).data
            })
        return Response({
            'message': 'Invalid credentials'
        }, status=status.HTTP_401_UNAUTHORIZED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema( tags=["Auth"])
class LoginView(TokenObtainPairView):
    serializer_class = TokenObtainPairView.serializer_class

@extend_schema(tags=["Auth"])
class RefreshTokenCustomView(TokenRefreshView):
    serializer_class = TokenRefreshView.serializer_class

@method_decorator(cache_page(60 * 5), name='dispatch')
@extend_schema(tags=['User'])
class UserViewSet(ListAPIView):
    serializer_class = UserInfoSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

@extend_schema(tags=['User'])
class LeaveTeamView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
       if request.user.leave_team():
           return Response({"detail": "You have successfully left the team."}, status=status.HTTP_200_OK)
       return Response({"detail": "You are not part of any team."}, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(tags=["Search"])
class SearchUserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserInfoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username']
    permission_classes = [AllowAny]