from rest_framework import serializers 
from .models import  *

class ProjectSerializer(serializers.ModelSerializer): 
  class Meta: 
    model = Project 
    fields = '__all__'

class ResumeSerializer(serializers.ModelSerializer): 
  class Meta: 
    model = Resume 
    fields = '__all__'

