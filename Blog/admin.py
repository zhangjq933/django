# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Article, Tag, Category

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
	list_display = ['title', 'created_time', 'modified_time', 'category', 'author']

admin.site.register(Article)
admin.site.register(Tag)
admin.site.register(Category)