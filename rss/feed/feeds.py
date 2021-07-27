from os import link
import feedparser as fp

from models import RssFeed, RssFeedItems

# from time import mktime
from datetime import datetime
from django.core.management.base import BaseCommand
from typing import Any


class Command(BaseCommand):
    args = ""
    help = "Get N recent news feed and save it in the RssfeedItem to improve load times of feed"

    def handle(self, args: Any, **options: Any):
        for rss in RssFeed.objects.all():
            feed = fp.parse(f"{rss.link}")
            num_feed = int(args)
            # max = num_feed if len(feed['entries']) > num_feed else len(feed['entries'])

            for i in range(0, 10):
                if feed[i]:
                    feed_post = RssFeedItems()
                    feed_post.title = feed.entries[i].title
                    feed_post.link = feed.entries[i].link
                    feed_post.desc = feed.entries[i].description
                    feed_post.created_at = feed.entries[i].pubDate
                    feed_post.thumbnail = feed.entries[i].image
                    feed_post.save()


# cron job:  * /30 * * * * /usr/bin/python3 /home/Document/WEBSOLUTIONS/rss/manage.py feeds 10
