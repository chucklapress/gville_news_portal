from django.contrib import admin
from app.models import HeadlineArticle
from app.models import LocalArticle
from app.models import SportsArticle
from app.models import BusinessArticle

# Register your models here.
admin.site.register(HeadlineArticle)
admin.site.register(LocalArticle)
admin.site.register(SportsArticle)
admin.site.register(BusinessArticle)
