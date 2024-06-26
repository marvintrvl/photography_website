# Generated by Django 5.0.6 on 2024-05-21 20:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0005_alter_photo_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='category',
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='photos.category')),
            ],
        ),
        migrations.AddField(
            model_name='photo',
            name='subcategory',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='photos.subcategory'),
            preserve_default=False,
        ),
    ]
