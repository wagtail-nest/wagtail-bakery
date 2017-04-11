import os

from django.conf import settings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

pytest_plugins = 'tests.fixtures'

def pytest_configure():
    settings.configure(
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        },
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

            'tests',
        ],
        MIDDLEWARE_CLASSES=[
            'django.middleware.security.SecurityMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.locale.LocaleMiddleware',
            'django.middleware.common.CommonMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
            'django.middleware.clickjacking.XFrameOptionsMiddleware',
            'wagtail.wagtailcore.middleware.SiteMiddleware',
            'wagtail.wagtailredirects.middleware.RedirectMiddleware',
        ],
        ROOT_URLCONF='tests.urls',
        TEMPLATES=[
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': [
                    os.path.join(BASE_DIR, 'templates'),
                ],
                'OPTIONS': {
                    'context_processors': [
                        'django.template.context_processors.debug',
                        'django.template.context_processors.request',
                        'django.contrib.auth.context_processors.auth',
                        'django.contrib.messages.context_processors.messages',
                    ],
                    'loaders': [
                        'django.template.loaders.filesystem.Loader',
                        'django.template.loaders.app_directories.Loader',
                    ]
                },
            },
        ],
        WAGTAIL_SITE_NAME='Wagtail Bakery',
        BUILD_DIR=os.path.join(BASE_DIR, 'build'),
        BAKERY_VIEWS=(
            'wagtailbakery.views.AllPagesView',
        ),
        CELERY_ALWAYS_EAGER=True,
    )
