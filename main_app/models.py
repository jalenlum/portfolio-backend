from django.db import models

# Create your models here.
class File(models.Model): 
  bytes = models.TextField() 
  filename = models.CharField(max_length=255) 
  mimetype = models.CharField(max_length=50) 

  def __str__(self): 
    return self.filename

class Projects(models.Model): 
  unique_id = models.CharField(max_length=100) 
  name = models.CharField(max_length=100) 
  date = models.CharField(max_length=100)
  role_or_description = models.CharField(max_length=100)
  skills = models.CharField(max_length=100)
  link = models.CharField(max_length=200)
  information_body = models.TextField(max_length=3000)
  image = models.ImageField(upload_to='main_app.File/bytes/filename/mimetype', null=True,help_text="Please compress image and convert type to webp before uploading. https://imagecompressor.com/, https://cloudconvert.com/webp-converter") 

  def __str__(self): 
    return self.name

  def delete(self, *args, **kwargs): 
    super(Projects, self).delete(*args, **kwargs) 
    File.objects.filter(filename = self.image.name).delete()