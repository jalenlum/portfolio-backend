from django.urls import path
from .views import index, GetProjects, GetProjectsPagination, GetResume

urlpatterns = [
    path("", index),
    path('api/projects/', GetProjects.as_view(), name='get-projects'),
    path('api/projects/pagination/', GetProjectsPagination.as_view(), name='get-projects-pagination'),
    path('api/resume/', GetResume.as_view(), name = 'get-resume'),
]