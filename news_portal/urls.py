"""news_portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from app.views import IndexView, RSSfeedView, SportsfeedView, CommunityfeedView, PostandCourierView, HeadlineCreateView, PostandCourierCreateView, SportsArticleCreateView, CommunityPublicationsCreateView
from django.conf.urls.static import static
from django.conf import settings
from app import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url, include
from rest_framework.authtoken import views
from portalapi.views import RSSfeedAPIView, RSSfeedDetailAPIView, PostNCourierAPIView, PostNCourierDetailAPIView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^', include('django.contrib.auth.urls')),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^$', IndexView.as_view(), name='index_view'),
    url(r'^rss_feed/$', RSSfeedView.as_view(), name='rss_feed_view'),
    url(r'^sports_feed/$', SportsfeedView.as_view(), name='sports_feed_view'),
    url(r'^community_feed/$', CommunityfeedView.as_view(), name='community_feed_view'),
    url(r'^postncourier/$', PostandCourierView.as_view(), name='postncourier_feed_view'),
    url(r'^headline_create/$',HeadlineCreateView.as_view(), name='headline_create_view'),
    url(r'^postcourier_create/$',PostandCourierCreateView.as_view(), name='postcourier_create_view'),
    url(r'^sports_create/$',SportsArticleCreateView.as_view(), name='sports_create_view'),
    url(r'^community_create/$',CommunityPublicationsCreateView.as_view(), name='community_create_view'),
    url(r'^api/headlines/$', RSSfeedAPIView.as_view(), name="rss_feed_api_view"),
    url(r'^api/headlines/(?P<pk>\d+)/$', RSSfeedDetailAPIView.as_view(), name="rss_feed_detail_api_view"),
    url(r'^api/postncourier/$', PostNCourierAPIView.as_view(), name="postncourier_api_view"),
    url(r'^api/postncourier/(?P<pk>\d+)/$', PostNCourierDetailAPIView.as_view(), name="postncourier_detail_api_view")


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
