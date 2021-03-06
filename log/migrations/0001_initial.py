# Generated by Django 2.1.4 on 2019-07-08 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LogItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255, verbose_name='報修主旨')),
                ('description', models.TextField(verbose_name='報修內容')),
                ('reporter', models.CharField(max_length=30, verbose_name='報修人')),
                ('phone', models.CharField(max_length=30, verbose_name='聯絡電話')),
                ('ctime', models.DateTimeField(auto_now_add=True, verbose_name='報修時間')),
                ('handler', models.CharField(max_length=30, verbose_name='處理人員')),
                ('status', models.IntegerField(choices=[(0, '待處理'), (1, '處理中'), (2, '已結案')], default=0, verbose_name='處理進度')),
                ('comment', models.TextField(verbose_name='處理說明')),
                ('utime', models.DateTimeField(auto_now=True, verbose_name='最後更新時間')),
            ],
        ),
    ]
