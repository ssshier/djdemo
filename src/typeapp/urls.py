from django.urls import path
from .views.views import index
from .views.user import UserView

urlpatterns = [
    path('hello', index, name='hello'),
    path('user', UserView.as_view(), name='user'),
    path('user/list', UserView().list, name='user'),
]
