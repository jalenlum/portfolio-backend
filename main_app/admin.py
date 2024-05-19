from django.contrib import admin
from .models import *

# Register your models here.
class ProjectsAdmin(admin.ModelAdmin): 
  def get_actions(self, request): 
    actions = super().get_actions(request) 
    if request.user.username[0].upper() != "J": 
      if "delete_selected" in actions: 
        del actions["delete_selected"] 
    return actions
  def __str__(self): 
    return self.name
  
admin.site.register(Project, ProjectsAdmin)
admin.site.register(Resume)
