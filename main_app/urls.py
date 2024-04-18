from django.urls import path
from .views import index, GetProjects

urlpatterns = [
    path("", index),
    path('api/projects/', GetProjects.as_view(), name='get-projects'),
]