from django.urls import path
from .views import *

urlpatterns = [
    path("product/", ProductLCView.as_view())
]