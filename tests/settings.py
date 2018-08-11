import os

import wagtail


def _wagtail_apps():
    if wagtail.VERSION >= (2, 0):
        return [
            'wagtail.contrib.forms',
            'wagtail.contrib.redirects',
            'wagtail.embeds',
            'wagtail.sites',
            'wagtail.users',
            'wagtail.snippets',
            'wagtail.documents',
            'wagtail.images',
            'wagtail.search',
            'wagtail.admin',
            'wagtail.core',
        ]
    else:
        return [
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
        ]

def _wagtail_middleware():
    if wagtail.VERSION >= (2, 0):
        return [
            'wagtail.core.middleware.SiteMiddleware',
            'wagtail.redirects.middleware.RedirectMiddleware',
        ]
    else:
        return [
            'wagtail.wagtailcore.middleware.SiteMiddleware',
            'wagtail.wagtailredirects.middleware.RedirectMiddleware',
        ]


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEBUG = True

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

] + _wagtail_apps() + [

    'modelcluster',
    'taggit',

    'bakery',
    'wagtailbakery',
    'tests',
]

LANGUAGES = [
    ('en', 'English'),
    ('nl', 'Dutch'),
]

LANGUAGE_CODE = 'en-us'

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'public/media')

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
] + _wagtail_middleware()

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)

ROOT_URLCONF = 'tests.urls'

SECRET_KEY = '7b&ova34-9b(dj$gevm65$lc!m3#^#g1z*v#gv-g8k0wlo7#l8'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'public/static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

TEMPLATES = [
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
]

TIME_ZONE = 'UTC'

USE_I18N = True
USE_L10N = True
USE_TZ = True

WAGTAIL_SITE_NAME = 'Wagtail Bakery'

BUILD_DIR = os.path.join(BASE_DIR, 'build')
BAKERY_VIEWS = (
    'wagtailbakery.views.AllPagesView',
)

CELERY_ALWAYS_EAGER = True
