# Generated by Django 4.1.3 on 2022-12-05 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="like",
            name="blog",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="blog.blog"
            ),
        ),
    ]
