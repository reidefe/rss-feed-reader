from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import RssFeedItems, RssFeed
from typing import Any, List
import feedparser
from django.http import HttpRequest, HttpResponse


class RssFeedItemsView(ListView):
    model = RssFeedItems
    queryset = RssFeedItems.objects.all()
    # paginate_by = 10
    template_name = "feeds.html"
    context_object_name = "feed_list"

    def get_queryset(self):
        links = RssFeed.objects.values_list("link", flat=True)
        for l in links:
            feed = feedparser.parse(l)
            for i in range(len(feed.entries)):
                feed_post = RssFeedItems()
                rssfeed_id = RssFeed.objects.get(link=l)
                feed_post.feed = rssfeed_id
                feed_post.title = feed.entries[i]["title"]
                feed_post.link = feed["entries"][i]["link"]
                feed_post.desc = feed["entries"][i]["description"]
                feed_post.created_at = feed["entries"][i]["published"]
                # feed_post.thumbnail = feed['entries'][i]['media_thumbnail']
                feed_post.save()
        items = RssFeedItems.objects.all()
        return items
