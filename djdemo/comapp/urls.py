from django.urls import path

from .views.com_exc import ComExcView

urlpatterns = [
    # com-exc
    path("com-exc", ComExcView.as_view(), name="com-exc"),
    path("com-exc/list", ComExcView().list, name="com-exc"),
]
