from django.urls import path

from .views import *
urlpatterns = [
    path('list/', UserListView.as_view()),
    path('myinfo/', MyInfoView.as_view()),
    path('signup/', UserCreateView.as_view()),
]