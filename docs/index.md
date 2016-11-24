# Wagtail bakery

A set of helpers for baking your Django Wagtail site out as flat files.

## Features

* Single management command that will build your Wagtail site out as flat files
* Support for multisite, [theming](https://github.com/moorinteractive/wagtail-themes) and [multilingual](http://docs.wagtail.io/en/latest/advanced_topics/i18n/index.html) setup
* Support for `i18n_patterns`
* Ready to use Wagtail Buildable views to build all your (un)published pages at once (no extra code required!)

## Troubleshooting

If you get an `DisallowedHost` error while running the `manage.py build` command, please add `testserver` to your `ALLOWED_HOSTS` settings.

For more issues [please submit an issue](https://github.com/moorinteractive/wagtail-bakery/issues/new) on GitHub.

## Credits

Thanks to [@mhnbcu](https://github.com/mhnbcu/wagtailbakery) for bringing this
idea up initially, and [Django Bakery](https://github.com/datadesk/django-bakery)
for providing the initial bakery package.
