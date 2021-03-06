# Generated by Django 2.1.7 on 2020-07-12 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='avg_rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='carrating',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.Car', verbose_name='car_model'),
        ),
    ]
