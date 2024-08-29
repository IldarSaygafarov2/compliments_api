from django.urls import path
from . import views


urlpatterns = [
    path('', views.ComplimentList.as_view())
]