# Wagtail-bakery

A set of helpers for baking your Django Wagtail site out as flat files.

## Status

[![Documentation Status](https://readthedocs.org/projects/wagtail-bakery/badge/?version=latest)](http://wagtail-bakery.readthedocs.io/en/latest/?badge=latest)
[![Build Status](https://travis-ci.org/moorinteractive/wagtail-bakery.svg?branch=master)](https://travis-ci.org/moorinteractive/wagtail-bakery)
[![Coverage Status](https://coveralls.io/repos/github/moorinteractive/wagtail-bakery/badge.svg?branch=master)](https://coveralls.io/github/moorinteractive/wagtail-bakery?branch=master)

## Features

* Support for `i18n_patterns`

## Installation

```
pip install wagtail-bakery
```

Add `bakery` and `wagtailbakery` to your `INSTALLED_APPS`.

If you get an error `DisallowedHost` while running the `manage.py build` command please add `testserver` to your `ALLOWED_HOSTS` settings.

## Credits

Thanks to [@mhnbcu](https://github.com/mhnbcu/wagtailbakery) for bringing this
idea up initially, and [Django Bakery](https://github.com/datadesk/django-bakery)
for providing the initial bakery package.
