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
from app.models import HeadlineArticle, SportsArticle


# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

class RSSfeedView(ListView):
    model = HeadlineArticle

class SportsfeedView(ListView):
    model = SportsArticle
