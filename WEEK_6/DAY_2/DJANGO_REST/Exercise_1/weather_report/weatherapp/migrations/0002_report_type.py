# Generated by Django 4.2.4 on 2023-08-14 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weatherapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='type',
            field=models.CharField(choices=[('su', 'sunny'), ('clo', 'cloudy'), ('wi', 'windy'), ('ra', 'rainy')], default=1, max_length=3),
            preserve_default=False,
        ),
    ]
