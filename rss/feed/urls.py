from django.urls import path
from .views import RssFeedItemsView

urlpatterns = [path("", RssFeedItemsView.as_view(), name="feed_list")]
