from django.contrib import admin
from blogapp.models import Blog,BlogComment

# Register your models here.
admin.site.register((Blog,BlogComment))
