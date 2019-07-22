from django.db import models

#from accounts.models import User
from django.contrib.auth import get_user_model
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

# category.product_set
# category.category_products
# user.product_set
DELIVERY_TYPES = (
    (1, '택배거래'),
    (2, '직거래'),
    (3, '택배/직거래'),
)
class Product(models.Model):

    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='category_products', verbose_name='카테고리')
    owner = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, related_name='my_products')
    title = models.CharField(max_length=100, verbose_name='제품명')
    slug = models.SlugField(unique=True, allow_unicode=True)
    image = models.ImageField(upload_to='products/')
    delivery = models.IntegerField(choices=DELIVERY_TYPES, verbose_name='거래 방법')
    description = models.TextField(verbose_name='제품 설명')
    price = models.IntegerField(verbose_name='제품 가격')
    active = models.BooleanField(default=True,verbose_name='구매 가능')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  self.title

# python manage.py makemigrations - 데이터베이스 반영할 내용을 추적해서 파일 만들기
# python manage.py migrate - 위에서 만든 파일을 가지고 실제 DB에 내용을 반영
RATE_CHOICE = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)
class Comment(models.Model):
    writer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='my_comments')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    rate = models.IntegerField(choices=RATE_CHOICE)
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
