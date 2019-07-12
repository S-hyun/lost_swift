from django.db import models

# Create your models here.

# 모델 : 데이터베이스에 어떤 자료를 어떤 형태로 저장할 것이냐 결정
# 모델을 항상 클래스 형태

"""
class 클래스이름(부모클래스):
    attribute
    method
"""

# 모델을 작성했다. -> DB 설계를 끝냈다.

# 1. 모델을 참조해서 -> DB에 반영할 내용을 찾는다.
# python manage.py makemigrations
# 2. DB에 반영할 내용을 -> 실제로 DB에 쿼리를 실행한다.
# python manage.py migrate

from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
class Blog(models.Model):
    # 작성자를 특정할 수 있는 정보 - email, username, 주민번호,
    # user의 index 번호
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=100)
    content = RichTextUploadingField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        from django.shortcuts import resolve_url
        return resolve_url("detail", self.id)
        # {% url 'detail' object.id %}