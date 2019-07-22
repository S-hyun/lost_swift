from django.contrib import admin

# Register your models here.
from .models import *
class CategoryOption(admin.ModelAdmin):
    list_display = ['id','name','slug']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryOption)

class ProductOption(admin.ModelAdmin):
    list_display = ['id','title','slug','owner','delivery','created','updated','active']
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Product, ProductOption)

from .models import *
class CommentOption(admin.ModelAdmin):
    list_display = ['id', 'writer', 'product', 'comment', 'rate', 'created']

admin.site.register(Comment, CommentOption)

#python manage.py makemigrations
# # python manage.py migrate