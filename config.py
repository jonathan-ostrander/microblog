import os
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = 'fundees99'

OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]
    
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
WHOOSH_BASE = os.path.join(basedir, 'search.db')
WHOOSH_ENABLED = os.environ.get('HEROKU') is None

# -*- coding: utf-8 -*-
# ...
# available languages
LANGUAGES = {
    'en': 'English',
}

# email server
MAIL_SERVER = 'smtp.google.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'jonathanost@gmail.com'
MAIL_PASSWORD = 'thequickbrownfoxjumpsoverthelazydog3141592653589'

# administrator list
ADMINS = ['jonathanost@gmail.com']

# pagination
POSTS_PER_PAGE = 3
MAX_SEARCH_RESULTS = 50
