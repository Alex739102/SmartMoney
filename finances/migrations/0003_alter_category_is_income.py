# Generated by Django 5.2.1 on 2025-05-13 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0002_alter_category_is_income'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='is_income',
            field=models.BooleanField(default=False),
        ),
    ]
