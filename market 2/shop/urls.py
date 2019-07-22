from django.urls import path
from .views import *


urlpatterns = [
    path("product/", ProductLCView.as_view()),
    path("comment/", CommentListView.as_view()),
    path("detail/<int:pk>/", ProductDetialView.as_view())
]