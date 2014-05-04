#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Oppten'
SITENAME = u'Oppten Blog'
SITEURL = 'http://oppten.github.io'
THEME = u'pelican-bootstrap3'
BOOTSTRAP_THEME = u''
TIMEZONE = 'America/Bogota'

DEFAULT_LANG = u'es'

# Feed generation is usually not desired when developing
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
AUTHOR_FEED_RSS = 'feeds/%s.rss.xml'
AUTHOR_FEED_RSS = 'feeds/%s.rss.xml'
TRANSLATION_FEED_RSS = 'feeds/all-%s.rss.xml'

# Blogroll
LINKS =  (('Oppten', 'http://oppten.com/'),
          ('VidaNP', 'http://vidanp.wordpress.com/'),
          ('Nasa', 'http://nasa.gov/'),
          ('Ypursite?', '#'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/oppten'),
          ('linkedin', 'https://www.linkedin.com/company/oppten'),
          ('github', 'http://github.com/oppten'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
