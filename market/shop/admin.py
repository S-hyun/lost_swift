from django.contrib import admin

# Register your models here.
from .models import *
class CatrgoryOption(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Cartegory, CatrgoryOption)

class ProductOption(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'owner', 'delivery', 'created', 'updated', 'active']
    prepopulated_fields = {'slug':('title',)}
admin.site.register(Product, ProductOption)