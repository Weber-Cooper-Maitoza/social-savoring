# Generated by Django 5.1.3 on 2024-12-04 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipies', '0004_alter_recipe_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_image',
            field=models.CharField(default='https://img.freepik.com/premium-vector/default-image-icon-vector-missing-picture-page-website-design-mobile-app-no-photo-available_87543-11093.jpg', max_length=500),
        ),
    ]
