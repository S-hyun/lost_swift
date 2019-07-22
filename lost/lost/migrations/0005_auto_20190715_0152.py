# Generated by Django 2.2.3 on 2019-07-15 01:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lost', '0004_auto_20190715_0134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='my_comments', to=settings.AUTH_USER_MODEL, verbose_name='아이디'),
        ),
    ]
