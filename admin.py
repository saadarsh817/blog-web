from django.contrib import admin
from geekymini.models import newpost,newimage

# Register your models here.
@admin.register(newpost)
#@admin.register(newimage)

class newadmin(admin.ModelAdmin):
    list_display=['id','title']
    
    def __str__(self):
        return self.title
    
@admin.register(newimage)
class new_admin(admin.ModelAdmin):
    list_display=['image','dates']
    
    def __str__(self):
        return self.dates

