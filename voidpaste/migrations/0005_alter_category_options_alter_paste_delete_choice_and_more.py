# Generated by Django 5.0.7 on 2024-07-20 14:58

import voidpaste.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("voidpaste", "0004_remove_category_description"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name": "Category", "verbose_name_plural": "Categories"},
        ),
        migrations.AlterField(
            model_name="paste",
            name="delete_choice",
            field=models.CharField(
                choices=[
                    ("10_minutes", "10 Minutes"),
                    ("1_hour", "1 Hour"),
                    ("1_day", "1 Day"),
                    ("1_week", "1 Week"),
                    ("2_weeks", "2 Weeks"),
                    ("never", "Never"),
                ],
                default="never",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="paste",
            name="link",
            field=models.SlugField(
                default=voidpaste.utils.generate_unique_link,
                editable=False,
                max_length=8,
                unique=True,
            ),
        ),
    ]
