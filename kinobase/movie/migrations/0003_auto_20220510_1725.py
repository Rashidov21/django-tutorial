# Generated by Django 3.2.6 on 2022-05-10 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_movie_poster'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='country',
            field=models.CharField(default='USA', max_length=50),
        ),
        migrations.AddField(
            model_name='movie',
            name='year',
            field=models.CharField(default='2022', max_length=5),
        ),
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(to='movie.Actor'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(to='movie.Genre'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(upload_to='movie_posters/%Y/%m'),
        ),
    ]