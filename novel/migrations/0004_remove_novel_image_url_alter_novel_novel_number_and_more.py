# Generated by Django 5.0.6 on 2024-07-01 16:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novel', '0003_novel_novel_number_novel_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='novel',
            name='image_url',
        ),
        migrations.AlterField(
            model_name='novel',
            name='novel_number',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='novel',
            name='number',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='NovelImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=256)),
                ('interval', models.IntegerField(default=5000)),
                ('novel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='novel.novel')),
            ],
        ),
    ]
