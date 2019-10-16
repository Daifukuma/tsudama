# Generated by Django 2.2.6 on 2019-10-13 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_lesson'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('comment', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='photos')),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]