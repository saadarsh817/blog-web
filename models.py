from django.db import models

# Create your models here.
class newpost(models.Model):
    title=models.CharField(max_length=150)
    description=models.TextField()
    

class newimage(models.Model):
    image=models.ImageField(upload_to="myimage")
    dates=models.DateTimeField(auto_now_add=True)


    