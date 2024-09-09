from django.urls import path
from .views import SignupView, SearchUsersView, FriendRequestView, PendingFriendRequestView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('search/', SearchUsersView.as_view(), name='search-users'),
    path('friend-requests/', FriendRequestView.as_view(), name='friend-requests'),
    path('pending-requests/', PendingFriendRequestView.as_view(), name='pending-requests'),
]
