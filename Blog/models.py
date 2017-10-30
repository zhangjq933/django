# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models  import User
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class Tag(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name

@python_2_unicode_compatible
class Category(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name

#class Article(models.Model):
#	url = models.URLField()
#	title = models.CharField(max_length=50)
#	title_zh = models.CharField(max_length=50)
#	author = models.CharField(max_length=30)
#	abstract = models.CharField(max_length=200, blank=True)
#	content_md = models.TextField()
#	content_html = models.TextField()
#	category = models.ForeignKey(Category)
#	tags = models.ManyToManyField(Tag, blank=True)
#	views = models.IntegerField()
#	created = models.DateTimeField()
#	updated = models.DateTimeField()

@python_2_unicode_compatible
class Article(models.Model):
	title = models.CharField(max_length=70)
	body = models.TextField()
	created_time = models.DateTimeField()
	modified_time = models.DateTimeField()
	abstract = models.CharField(max_length=200, blank=True)
	category = models.ForeignKey(Category)
	tags = models.ManyToManyField(Tag, blank=True)
	author = models.ForeignKey(User)
	views = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('detail', kwargs={'pk': self.pk})

	def increase_views(self):
		self.views += 1
		self.save(update_fields=['views'])




		