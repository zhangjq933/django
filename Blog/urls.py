from django.conf.urls import url
import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^test', views.test, name='test'),
	url(r'^index', views.index, name='index'),
	url(r'^article/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
	url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
	url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
  #url(r'^blog_base', views.blog_base),
]
  