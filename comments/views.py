# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from Blog.models import Article

from .models import Comment
from .forms import CommentForm
# Create your views here.

def article_comment(request, article_pk):
	article = get_object_or_404(Article, pk=article_pk)
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.article = article
			comment.save()
			return redirect(article)
		else:
			comment_list = article.comment_set.all()
			context = {
						'article':article,
						'form':form,
						'comment_list':comment_list,
			}
			return render(request, 'Blog/detail.html', context=context)
		return redirect(article)