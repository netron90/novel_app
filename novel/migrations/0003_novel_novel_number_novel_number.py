# Generated by Django 5.0.6 on 2024-07-01 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novel', '0002_novel_location_novel_mail_contact_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='novel',
            name='novel_number',
            field=models.CharField(blank=True, editable=False, max_length=16),
        ),
        migrations.AddField(
            model_name='novel',
            name='number',
            field=models.PositiveIntegerField(default=1, editable=False),
        ),
    ]
