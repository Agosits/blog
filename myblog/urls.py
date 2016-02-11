"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from journal import views as journal_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',journal_views.index),
    url(r'^new_journal/$',journal_views.new_journal),
    url(r'^test/$',journal_views.test),
    url(r'^comment/$',journal_views.show_comment),
    url(r'^journal/(\d{1,2})/$',journal_views.journal_content),
    url(r'^tag/(.+)/$',journal_views.show_tag),
    url(r'^logout/$',journal_views.logout_view),
    url(r'^page/(\d{1,2})/$',journal_views.show_journal),
]
