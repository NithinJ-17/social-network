from rest_framework import generics, permissions
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import FriendRequest
from .serializers import UserSerializer, FriendRequestSerializer

# Signup API
class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

# Search Users API
class SearchUsersView(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q')
        if '@' in query:  # Search by email
            return User.objects.filter(email__iexact=query)
        else:  # Search by name
            return User.objects.filter(username__icontains=query)

# Friend Request API
class FriendRequestView(generics.ListCreateAPIView):
    serializer_class = FriendRequestSerializer

    def get_queryset(self):
        user = self.request.user
        return FriendRequest.objects.filter(from_user=user)

# List Pending Requests API
class PendingFriendRequestView(generics.ListAPIView):
    serializer_class = FriendRequestSerializer

    def get_queryset(self):
        user = self.request.user
        return FriendRequest.objects.filter(to_user=user, status='pending')
