# Generated by Django 4.1.7 on 2023-02-28 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('show_book', '0002_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='RatingBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('choice_show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_object', to='show_book.showbook')),
            ],
        ),
    ]