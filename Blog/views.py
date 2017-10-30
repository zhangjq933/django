# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import markdown
from django.shortcuts import render, get_object_or_404
from .models import Article, Category
from comments.forms import CommentForm

# Create your views here.

def home(request):
	context = {
		'text': 'just for test',
		'welcome': 'hello world.'
	}
	return render(request, 'home.html', context)

def archives(request, year, month):
	article_list = Article.objects.filter(created_time__year=year,created_time__month=month).order_by('-created_time')
	#article_list = Article.objects.order_by('-created_time')
	return render(request, 'index.html', context={'article_list': article_list})
#def blog_base(request):
#  return render(request, 'blog_base.html')
def test(request):
	return render(request, 'test.html')

def index(request):
	article_list = Article.objects.all().order_by('-created_time')
	return render(request, 'index.html', context={'article_list': article_list})

def detail(request, pk):
	article = get_object_or_404(Article, pk=pk)
	article.increase_views()
	article.body = markdown.markdown(article.body,
		extensions =[
			'markdown.extensions.extra',
			'markdown.extensions.codehilite',
			'markdown.extensions.toc',
		])
	form = CommentForm()
	comment_list = article.comment_set.all()
	context = {
		'article':article,
		'form':form,
		'comment_list':comment_list,
	}
	return render(request, 'detail.html', context=context)

def category(request, pk):
	cate = get_object_or_404(Category, pk=pk)
	article_list = Article.objects.filter(category=cate).order_by('-created_time')
	return render(request, 'index.html', context={'article_list': article_list})

