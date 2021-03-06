# Generated by Django 3.2.5 on 2021-07-26 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="RssFeed",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("link", models.CharField(max_length=255)),
                ("created_at", models.DateTimeField(auto_now=True)),
            ],
            options={"ordering": ["created_at"]},
        ),
        migrations.CreateModel(
            name="RssFeedItems",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("link", models.CharField(max_length=255)),
                ("thumbnail", models.ImageField(upload_to="")),
                ("desc", models.TextField(blank=True, null=True)),
                ("slug", models.SlugField(max_length=255)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "feed",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="feed.rssfeed",
                    ),
                ),
            ],
            options={"ordering": ["-created_at"]},
        ),
    ]
