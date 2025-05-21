from django.urls import path

from userextend.views import UserCreateView, UserLoginView

urlpatterns = [
    path('register/',UserCreateView.as_view(),name='user_create'),
    path('login/',UserLoginView.as_view(),name='user_login'),
]