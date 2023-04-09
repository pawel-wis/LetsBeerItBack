from django.urls import path
from .views import hello, UsersListView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', hello),
    path('users', UsersListView.as_view()),
    path('users/get-token', obtain_auth_token, name='get-token'),
]
