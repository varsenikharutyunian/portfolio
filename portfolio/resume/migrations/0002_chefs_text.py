# Generated by Django 3.2.18 on 2023-09-20 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chefs',
            name='text',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
