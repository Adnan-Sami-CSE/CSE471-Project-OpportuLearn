# Generated by Django 4.2.7 on 2023-12-03 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0003_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitorNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification', models.CharField(max_length=1000)),
            ],
        ),
    ]
