from django.contrib import admin

# Register your models here.
# 작성한 모델을 관리자페이지에서 다룰 수 있도록 등록하는 파일

from .models import Blog

class BlogOption(admin.ModelAdmin):
    list_display = ['id', 'writer', 'title', 'created', 'updated']

admin.site.register(Blog, BlogOption)