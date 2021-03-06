# Generated by Django 3.1.5 on 2021-01-16 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210110_1732'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-comment_date',)},
        ),
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(verbose_name='التعليق'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='البريد الالكتروني'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=50, verbose_name='الاسم'),
        ),
    ]
