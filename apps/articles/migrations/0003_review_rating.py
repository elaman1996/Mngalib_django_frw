# Generated by Django 4.2 on 2023-04-07 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=1, default=0.0, max_digits=2),
        ),
    ]