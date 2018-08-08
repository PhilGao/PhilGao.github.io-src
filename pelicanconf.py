#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'PhilGao'
SITENAME = 'PhilGao Blog'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['images']

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'Chinese (Simplified)'
RELATIVE_URLS = 'False'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/')
		 )

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DISQUS_SITENAME = "gaohao"

DEFAULT_PAGINATION = 10

THEME = "pelican-elegant-1.3"
SITESUBTITLE = "行百里者半九十"
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
#AboutMe Page & Project Pages
LANDING_PAGE_ABOUT = {'title': 'PhilGao Blog','details':'尘世中一迷途小书僮，数据菜鸟，魔兽粉'}
PROJECTS = [{
    'name': 'Not Yet',
    'url': '',
    'description': 'Not Yet'}]
#plugin setting
PLUGIN_PATHS = ['F:\pelican-plugins']
PLUGINS = ['sitemap', 'extract_toc', 'tipue_search']
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
#site license
#SITE_LICENSE = 'by PhilGao is licensed under a Creative Commons Attribution-ShareAlike 3.0 Unported License'

# Elegant Labels
COMMENTS_INTRO = 'So what do you think? Did I miss something? Is any part unclear? Leave your comments below.'