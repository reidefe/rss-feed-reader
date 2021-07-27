from os import name
from django.db import models
from django.contrib.auth.models import User
from django.db.models.expressions import OrderBy
from django.urls import reverse
from django.template.defaultfilters import slugify


class RssFeed(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self) -> str:
        return self.name


class RssFeedItems(models.Model):
    title = models.CharField(max_length=255)
    feed = models.ForeignKey(RssFeed, on_delete=models.PROTECT, blank=True)
    link = models.CharField(max_length=255)
    thumbnail = models.ImageField()
    desc = models.TextField(null=True, blank=True)
    slug = models.SlugField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("feed_list", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
