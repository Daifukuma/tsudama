# Generated by Django 2.2.6 on 2019-10-24 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='textbook',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='market.Department', verbose_name='使用する学科'),
        ),
        migrations.AlterField(
            model_name='textbook',
            name='schoolyear',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='market.Schoolyear', verbose_name='推奨学年'),
        ),
        migrations.AlterField(
            model_name='textbook',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='market.Status', verbose_name='状態'),
        ),
    ]
