from django.shortcuts import render
from rest_framework.views import APIView 
from .serializers import * 
from rest_framework.response import Response


# Create your views here.
def index(request):
    return render(request, "index.html")

class GetProjects(APIView): 
  def get(self, request): 
    queryset=Project.objects.prefetch_related("image").all() 
    serializer = ProjectSerializer(queryset,many=True,context={'request': request})
    return Response(serializer.data)