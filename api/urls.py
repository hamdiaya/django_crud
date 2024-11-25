from django.urls import path
from .views import getUsers , createUser , user_detail



urlpatterns = [
path('users/' , getUsers ,name = 'get users'),
path('users/create/' , createUser ,name = 'create user'),
path('users/<int:pk>' , user_detail ,name = ' user details')
]