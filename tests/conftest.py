import os

from django.conf import settings


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def pytest_configure():
    settings.configure(
        BAKERY_VIEWS=[],
        BUILD_DIR=os.path.join(BASE_DIR, 'build'),
        INSTALLED_APPS=[
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',

            'wagtail.wagtailforms',
            'wagtail.wagtailredirects',
            'wagtail.wagtailembeds',
            'wagtail.wagtailsites',
            'wagtail.wagtailusers',
            'wagtail.wagtailsnippets',
            'wagtail.wagtaildocs',
            'wagtail.wagtailimages',
            'wagtail.wagtailsearch',
            'wagtail.wagtailadmin',
            'wagtail.wagtailcore',

            'modelcluster',
            'taggit',

            'bakery',
            'wagtailbakery',
        ],
        MEDIA_ROOT=os.path.join(BASE_DIR, 'public/media'),
        MEDIA_URL='/media/',
        STATIC_ROOT=os.path.join(BASE_DIR, 'public/static'),
        STATIC_URL='/static/',
    )
