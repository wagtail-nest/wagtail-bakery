# Wagtail-bakery

A set of helpers for baking your Django Wagtail site out as flat files.

[![Documentation Status](https://readthedocs.org/projects/wagtail-bakery/badge/?version=latest)](http://wagtail-bakery.readthedocs.io/en/latest/?badge=latest)
[![Build Status](https://travis-ci.org/moorinteractive/wagtail-bakery.svg?branch=master)](https://travis-ci.org/moorinteractive/wagtail-bakery)
[![Coverage Status](https://coveralls.io/repos/github/moorinteractive/wagtail-bakery/badge.svg?branch=master)](https://coveralls.io/github/moorinteractive/wagtail-bakery?branch=master)

* Documentation: [https://wagtail-bakery.readthedocs.io](https://wagtail-bakery.readthedocs.io)
* Issues: [https://github.com/moorinteractive/wagtail-bakery/issues](https://github.com/moorinteractive/wagtail-bakery/issues)
* Testing: [https://travis-ci.org/moorinteractive/wagtail-bakery](https://travis-ci.org/moorinteractive/wagtail-bakery)
* Coverage: [https://coveralls.io/github/moorinteractive/wagtail-bakery](https://coveralls.io/github/moorinteractive/wagtail-bakery)

Wagtail-bakery is build on top of [Django bakery](https://github.com/datadesk/django-bakery). Please read their [documentation](https://django-bakery.readthedocs.io/en/latest/) for detailed configuration and howto build default Django flat files. Yes. Wagtail-bakery is not limited to build Wagtail pages specifically, mixed content is possible!

## Features

* Single management command that will build your Wagtail site out as flat files
* Support for multisite, [theming](https://github.com/moorinteractive/wagtail-themes) and [multilingual](http://docs.wagtail.io/en/latest/advanced_topics/i18n/index.html) setup
* Support for `i18n_patterns`
* Ready to use Wagtail Buildable views to build all your (un)published pages at once (no extra code required!)

## Installation

```
pip install git+https://github.com/moorinteractive/wagtail-bakery.git#egg=wagtail-bakery
```

Add `bakery` and `wagtailbakery` to your `INSTALLED_APPS` setting.

```python
INSTALLED_APPS = (
    # ...
    'bakery',
    'wagtailbakery',
)
```

## Configuration

Add the build directory where you want to be the site be built as flat files.

```python
BUILD_DIR = '/tmp/build/'
```

As you are mabye known with Django bakery, the trickest part is to make your current models/pages buildable with [Buildable views](https://django-bakery.readthedocs.io/en/latest/buildableviews.html). As Django Wagtail uses only the `Page` model at their lowest level, you can use at least one of the already present Buildable views provided by Wagtail bakery.

Build all published public pages (use for production).

```python
BAKERY_VIEWS = (
	'wagtailbakery.views.AllPublishedPagesView',
)
```

Build all published and unpublished public pages (use for staging/acceptance).

```python
BAKERY_VIEWS = (
	'wagtailbakery.views.AllPagesView',
)
```

## Usage

Build the site out as flat files by running the `build` management command.

```
manage.py build
```

If you want to check how your static website will look like, use the `buildserver` after you have build your static files once.

```
manage.py buildserver
```

Please see the [documentation](https://wagtail-bakery.readthedocs.io) at for more information how to use Wagtail bakery.

## Examples

In the [examples](https://github.com/moorinteractive/wagtail-bakery/tree/master/examples) directory you can find a Wagtail setup with fixtures for a single site as well as a multisite setup.

Create a virtualenv and go to one of the examples, you can use the `Make` command to install all requirements, load fixtures and run the server.

Use as described in the usage section `manage.py build` to build the example out as static files.

## Troubleshooting

If you get an `DisallowedHost` error while running the `manage.py build` command, please add `testserver` to your `ALLOWED_HOSTS` settings.

For more issues [please submit an issue](https://github.com/moorinteractive/wagtail-bakery/issues/new) on GitHub.

## Credits

Thanks to [@mhnbcu](https://github.com/mhnbcu/wagtailbakery) for bringing this
idea up initially, and [Django Bakery](https://github.com/datadesk/django-bakery)
for providing the initial bakery package.
