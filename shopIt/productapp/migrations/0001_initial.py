# Generated by Django 5.0.2 on 2024-02-11 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('detail', models.CharField(max_length=500)),
                ('price', models.IntegerField()),
                ('cat', models.IntegerField()),
                ('is_active', models.BooleanField(default=1)),
            ],
        ),
    ]
