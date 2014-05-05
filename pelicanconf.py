#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Oppten'
SITENAME = u''
#SITEURL = 'http://blog.oppten.com'
THEME = u'pelican-bootstrap3'
BOOTSTRAP_THEME = u'oppten'
CUSTOM_CSS = u'static/custom.css'
FAVICON = u'images/favicon.png'
TIMEZONE = 'America/Bogota'
SHOW_ARTICLE_AUTHOR = True
SHOW_ARTICLE_CATEGORY = True
DEFAULT_LANG = u'es'

# Feed generation is usually not desired when developing
FEED_ALL_RSS = u'feeds/all.rss.xml'
GOOGLE_ANALYTICS = u'UA-32657044-1'
CATEGORY_FEED_RSS = u'feeds/%s.rss.xml'
AUTHOR_FEED_RSS = u'feeds/%s.rss.xml'
AUTHOR_FEED_RSS = u'feeds/%s.rss.xml'
SUBCATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
TRANSLATION_FEED_RSS = u'feeds/all-%s.rss.xml'
CC_LICENSE = u'CC-BY-NC-SA'
DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_BREADCRUMBS = False
DISPLAY_CATEGORY_IN_BREADCRUMBS = False
SITELOGO = u'images/logo.png'
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
MENUITEMS = (('Oppten','http://oppten.com'),)
TWITTER_USERNAME = u'oppten'
TWITTER_WIDGET_ID = u'463306257357484034'
ADDTHIS_PROFILE = U'ra-536686c31796168b'
PELICAN_COMMENT_SYSTEM = True
DISQUS_SITENAME =  u'oppten.disqus.com'
PLUGIN_PATH = 'pelican-plugins'
PLUGINS = ['assets', 'sitemap', 'gravatar', 'related_posts', 'liquid_tags', 'gallery','multi_part','neighbors', 
	   'pelican_vimeo', 'pelican_youtube','simple_footnotes','post_stats']
#stats, comments, subcategory
# Blogroll
LINKS =  (('Oppten', 'http://oppten.com/'),
          ('VidaNP', 'http://vidanp.wordpress.com/'),
          ('Nasa', 'http://nasa.gov/'),
          ('SocialAtom', 'http://socialatomgroup.com/'),
          ('NxtpLabs', 'http://nxtplabs.com/'),
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
