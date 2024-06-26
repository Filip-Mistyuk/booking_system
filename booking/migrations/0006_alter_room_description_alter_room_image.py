# Generated by Django 5.0 on 2024-04-28 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_room_image_delete_roomimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='description',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='room',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/'),
        ),
    ]
