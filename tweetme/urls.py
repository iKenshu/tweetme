from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from tweets.views import TweetListView
from hashtags.views import HashTagView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TweetListView.as_view(), name='home'),
    url(r'^tweets/', include('tweets.urls', namespace='tweets')),
    url(r'^tags/(?P<hashtag>.*)/$', HashTagView.as_view(), name='hashtags'),
    url(r'^api/tweets/', include('tweets.api.urls', namespace='tweets-api')),
    url(r'^api/', include('accounts.api.urls', namespace='profiles-api')),
    url(r'^', include('accounts.urls', namespace='profiles')),
]

if settings.DEBUG:
    urlpatterns += (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
