from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView,View,CreateView,ListView
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django import forms
from app.models import HeadlineArticle, SportsArticle, BusinessArticle, LocalArticle


# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

class RSSfeedView(ListView):
    model = HeadlineArticle

class SportsfeedView(ListView):
    model = SportsArticle

class MoneyfeedView(ListView):
    model = BusinessArticle

class LocalfeedView(ListView):
    model = LocalArticle

class HeadlineCreateView(CreateView):
    model = HeadlineArticle
    fields = ['top_stories_today','second_lede_today','third_lede_today']
    success_url = '/'

class BusinessArticleCreateView(CreateView):
    model = BusinessArticle
    fields = ['top_business_today','other_business_today']
    success_url = '/'

class LocalArticleCreateView(CreateView):
    model = LocalArticle
    fields = ['top_local_today','other_local_today']
    success_url = '/'

class SportsArticleCreateView(CreateView):
    model = SportsArticle
    fields = ['top_sports_today','other_sports_today']
    success_url = '/'
