# Generated by Django 5.0 on 2024-01-03 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ronin', '0005_cricket_delete_kabadi'),
    ]

    operations = [
        migrations.CreateModel(
            name='kabadi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelTable(
            name='cricket',
            table='kabadi',
        ),
    ]