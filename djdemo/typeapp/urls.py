from django.urls import path
from .views.views import index
from .views.user import (
    UserView,
    UserByUsernameView,
    UserByEmailView,
    UserPasswordChangeView,
)

urlpatterns = [
    path("hello", index, name="hello"),
    path("user", UserView.as_view(), name="user"),
    path("user/list", UserView().list, name="user"),
    path("user/get_by_username", UserByUsernameView.as_view(), name="user"),
    path("user/get_by_email", UserByEmailView.as_view(), name="user"),
    path("user/change_password", UserPasswordChangeView.as_view(), name="user"),
]
