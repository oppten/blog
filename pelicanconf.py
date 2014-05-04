#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Oppten'
SITENAME = u'Oppten Blog'
SITEURL = 'http://blog.oppten.com'
THEME = u'pelican-bootstrap3'
BOOTSTRAP_THEME = u'cerulean'
FAVICON = u'images/favicon.png'
TIMEZONE = 'America/Bogota'

DEFAULT_LANG = u'es'

# Feed generation is usually not desired when developing
FEED_ALL_RSS = u'feeds/all.rss.xml'
CATEGORY_FEED_RSS = u'feeds/%s.rss.xml'
AUTHOR_FEED_RSS = u'feeds/%s.rss.xml'
AUTHOR_FEED_RSS = u'feeds/%s.rss.xml'
TRANSLATION_FEED_RSS = u'feeds/all-%s.rss.xml'
CC_LICENSE = u'CC-BY-NC-SA'
DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True
SITELOGO = u'images/logo.png'
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True

# Blogroll
LINKS =  (('Oppten', 'http://oppten.com/'),
          ('VidaNP', 'http://vidanp.wordpress.com/'),
          ('Nasa', 'http://nasa.gov/'),
         )

# Social widget
SOCIAL = (('Twitter', 'http://twitter.com/oppten'),
	  ('Facebook', 'http://facebook.com/oppten'),
          ('Linkedin', 'https://www.linkedin.com/company/oppten'),
          ('Github', 'http://github.com/oppten'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ["images", ]
