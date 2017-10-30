from django.db.models.aggregates import Count
from ..models import Article, Category
from django import template

register = template.Library()

@register.simple_tag
def get_recent_articles(num=5):
	return Article.objects.all().order_by('-created_time')[:num]

@register.simple_tag
def archives():
	return Article.objects.dates('created_time', 'month', order='DESC')

@register.simple_tag
def get_categories():
	return Category.objects.annotate(num_posts=Count('article')).filter(num_posts__gt=0)
