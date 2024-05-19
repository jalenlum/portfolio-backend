from django.db import models

# Create your models here.
class File(models.Model): 
  bytes = models.TextField() 
  filename = models.CharField(max_length=255) 
  mimetype = models.CharField(max_length=50) 

  def __str__(self): 
    return self.filename

class Project(models.Model): 
  name = models.CharField(max_length=100, help_text="Enter the project or organization's name.") 
  unique_id = models.CharField(max_length=100, help_text="Enter an unique id.")
  image = models.ImageField(upload_to='main_app.File/bytes/filename/mimetype', null=True,help_text="Please compress logo and convert type to webp before uploading. https://imagecompressor.com/, https://cloudconvert.com/webp-converter") 
  date = models.CharField(max_length=100, default="", help_text="Enter the the start and end date (present if in progress).")
  description_or_role = models.CharField(max_length=100, default="", help_text="Enter the description of the project or your role in the organization.")
  skills = models.CharField(max_length=100, help_text="Enter the technical skills used.")
  link = models.CharField(max_length=200, help_text="Enter the link to the final product or to the organization's home page.")
  information_body = models.TextField(max_length=3000, help_text="Enter a detailed description of the project or organization.")

  def __str__(self): 
    return self.name

  def delete(self, *args, **kwargs): 
    super(Project, self).delete(*args, **kwargs) 
    File.objects.filter(filename = self.image.name).delete()

class Resume(models.Model):
  name = models.CharField(max_length=255)
  file = models.FileField(upload_to='main_app.File/bytes/filename/mimetype')

  def delete(self, *args, **kwargs):
    super(Resume, self).delete(*args, **kwargs)
    File.objects.filter(filename = self.file.name).delete()

  def __str__(self):
    return str(self.name)