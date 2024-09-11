from django.contrib import admin
from .models import Image

# Register your models here.


admin.site.register(Image)
class ImageAdmin(admin.ModelAdmin):
    display_list = ['id','photo','date']