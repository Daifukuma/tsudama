# Generated by Django 2.2.6 on 2019-10-23 12:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Schoolyear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Textbook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='タイトル')),
                ('image', models.ImageField(upload_to='textbooks', verbose_name='画像')),
                ('department', models.IntegerField(choices=[(1, '共通科目'), (2, '外国語科目'), (3, '健康余暇科学科目'), (4, '英語英文学科'), (5, '国際関係学科'), (6, '数学科'), (7, '情報科学科')], default=1, verbose_name='使用する学科')),
                ('schoolyear', models.IntegerField(choices=[(1, '1年生'), (2, '2年生'), (3, '3年生'), (4, '4年生')], default=1, verbose_name='推奨学年')),
                ('comment', models.TextField(blank=True, verbose_name='コメント')),
                ('status', models.IntegerField(choices=[(1, '新品同様'), (2, '汚れ、折り線有り'), (3, '書き込み有り')], default=1, verbose_name='状態')),
                ('point', models.PositiveIntegerField(default=300, verbose_name='価格')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='投稿日')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='market.Lesson', verbose_name='使用授業')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]