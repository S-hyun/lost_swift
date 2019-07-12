from django.urls import path

from .views import *

urlpatterns = [
    path("delete/<int:pk>/", BlogDelete.as_view(), name='delete'),
    path("update/<int:pk>/", BlogUpdate.as_view(), name='update'),
    path("create/", BlogCreate.as_view(), name="create"),
    path("detail/<int:pk>/", BlogDetail.as_view(), name="detail"),
    path("", BlogList.as_view(), name="index"),
]