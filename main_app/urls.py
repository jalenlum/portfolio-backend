from django.urls import path
from .views import index, GetProjects, GetProjectsPagination

urlpatterns = [
    path("", index),
    path('api/projects/', GetProjects.as_view(), name='get-projects'),
    path('api/programming-languages/pagination/', GetProjectsPagination.as_view(), name='get-projects-pagination')
]