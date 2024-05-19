from django.shortcuts import render
from rest_framework.views import APIView 
from .serializers import * 
from rest_framework.response import Response
from .pagination import ProjectPagination
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from Vercel!</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)

class GetProjects(APIView): 
  def get(self, request): 
    queryset=Project.objects.all() 
    serializer = ProjectSerializer(queryset,many=True,context={'request': request})
    return Response(serializer.data)
  
class GetProjectsPagination(APIView): 
  pagination_class = ProjectPagination 
  def get(self, request, *args, **kwargs): 
    queryset=Project.objects.prefetch_related("images").all() 
    paginator = self.pagination_class()
  
    page = paginator.paginate_queryset(queryset, request) 
    if page is not None: 
      serializer = ProjectSerializer(page, many=True) 
      return paginator.get_paginated_response(serializer.data) 
    serializer = ProjectSerializer(queryset, many=True) 
    return Response(serializer.data)
  
class GetResume(APIView): 
  def get(self, request): 
    queryset = Resume.objects.all()
    serializer = ResumeSerializer(queryset, many=True, context={'request': request})
    return Response(serializer.data)