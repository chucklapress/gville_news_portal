from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class HeadlineArticle(models.Model):
    top_stories_today = models.TextField(max_length=None)
    def __str__(self):
        return self.top_stories_today

class LocalArticle(models.Model):
    top_local_today = models.TextField(max_length=None)
    second_PandC_story = models.TextField(max_length=None, blank=True)
    third_PandC_story = models.TextField(max_length=None, blank=True)
    def __str__(self):
        return self.top_local_today

class SportsArticle(models.Model):
    top_sports_today = models.TextField(max_length=None)
    def __str__(self):
        return self.top_sports_today

class BusinessArticle(models.Model):
    top_business_today = models.TextField(max_length=None)
    second_community_story = models.TextField(max_length=None, blank=True)
    third_community_story = models.TextField(max_length=None, blank=True)
    def __str__(self):
        return self.top_business_today
