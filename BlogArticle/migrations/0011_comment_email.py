# Generated by Django 4.2 on 2023-05-11 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogArticle', '0010_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]