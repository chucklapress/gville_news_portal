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
from app.views import IndexView, RSSfeedView, SportsfeedView, MoneyfeedView, LocalfeedView, HeadlineCreateView, LocalArticleCreateView, SportsArticleCreateView, BusinessArticleCreateView
from django.conf.urls.static import static
from django.conf import settings
from app import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^', include('django.contrib.auth.urls')),
    url(r'^$', IndexView.as_view(), name='index_view'),
    url(r'^rss_feed/$', RSSfeedView.as_view(), name='rss_feed_view'),
    url(r'^sports_feed/$', SportsfeedView.as_view(), name='sports_feed_view'),
    url(r'^money_feed/$', MoneyfeedView.as_view(), name='money_feed_view'),
    url(r'^local_feed/$', LocalfeedView.as_view(), name='local_feed_view'),
    url(r'^headline_create/$',HeadlineCreateView.as_view(), name='headline_create_view'),
    url(r'^local_create/$',LocalArticleCreateView.as_view(), name='local_create_view'),
    url(r'^sports_create/$',SportsArticleCreateView.as_view(), name='sports_create_view'),
    url(r'^business_create/$',BusinessArticleCreateView.as_view(), name='business_create_view'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
