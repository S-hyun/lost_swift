from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class Cartegory(models.Model):
    name = models.CharField(max_length= 100, unique= True)
    slug = models.SlugField(unique=True, allow_unicode=True)
# category.protect_set
# user.product_set
DELIVERY_TYPES = (
    (1, '택배거래'),
    (2, '직거래'),
    (3, '택배/직거래'),
)
class Product(models.Model):
    category = models.ForeignKey(Cartegory, on_delete=models.PROTECT, related_name='category_products', verbose_name='카테고리')
    owner = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, related_name='my_products')
    title = models.CharField(max_length=100, verbose_name='제품명')
    slug = models.SlugField(unique=True, allow_unicode=True)
    image = models.ImageField(upload_to='products/')
    delivery = models.IntegerField(choices=DELIVERY_TYPES, verbose_name='거래 방법')
    description = models.TextField(verbose_name='제품 설명')
    price = models.IntegerField(verbose_name='제품 가격')
    active = models.BooleanField(default=True, verbose_name='구매 가능')
    created = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

# python manage.py makemigrations - 데이터베이스 반영할 내용을 추가해서 파일 만들기
#  python manage.py migrate - 위에서 만든 파일을 가지고 실제 DB에 내용을 반