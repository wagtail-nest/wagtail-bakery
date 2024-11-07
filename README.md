# Wagtail-bakery

A set of helpers for baking your Django Wagtail site out as flat files.

[![License: MIT](https://img.shields.io/pypi/l/wagtail-bakery)](https://github.com/wagtail-nest/wagtail-bakery/blob/main/LICENSE)
[![Build Status](https://github.com/wagtail-nest/wagtail-bakery/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/wagtail-nest/wagtail-bakery/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/wagtail-nest/wagtail-bakery/graph/badge.svg?token=5SbMtmHcal)](https://codecov.io/gh/wagtail-nest/wagtail-bakery)
[![Version](https://img.shields.io/pypi/v/wagtail-bakery.svg)](https://pypi.python.org/pypi/wagtail-bakery/)
[![Monthly downloads](https://img.shields.io/pypi/dm/wagtail-bakery.svg?logo=Downloads)](https://pypi.python.org/pypi/wagtail-bakery/)

Wagtail-bakery is built on top of [Django bakery](https://github.com/datadesk/django-bakery). Please read their [documentation](https://palewi.re/docs/django-bakery/) for detailed configuration and how to build default Django flat files. Yes. Wagtail-bakery is not limited to build Wagtail pages specifically, mixed content is possible!

## Links

- [Issues](https://github.com/wagtail-nest/wagtail-bakery/issues)
- [Discussion boards](https://github.com/wagtail/wagtail/discussions) are open for sharing ideas and plans for the Wagtail project.
- [Changelog](https://github.com/wagtail-nest/wagtail-bakery/issues)

### Security

We take the security of Wagtail, and related packages we maintain, seriously. If you have found a security issue with any of our projects please email us at [security@wagtail.org](mailto:security@wagtail.org) so we can work together to find and patch the issue. We appreciate responsible disclosure with any security related issues, so please contact us first before creating a GitHub issue.

If you want to send an encrypted email (optional), the public key ID for security@wagtail.org is 0xbed227b4daf93ff9, and this public key is available from most commonly-used keyservers.

## Features

- Single management command that will build your Wagtail site out as flat files
- Support for multisite, [theming](https://github.com/wagtail/wagtail-themes) and [multilingual](https://docs.wagtail.org/en/latest/advanced_topics/i18n.html) setup
- Support for `i18n_patterns`
- Support for generating a static API
- Ready to use Wagtail Buildable views to build all your (un)published pages at once (no extra code required!)

## Supported Versions

- Python 3.8 - 3.12
- Django 4.2 - 5.0
- Wagtail >= 5.2

We aim to support the Wagtail versions as [supported](http://docs.wagtail.org/en/latest/releases/upgrading.html) by Wagtail (current LTS, current stable).

Django/Wagtail combinations as [supported](http://docs.wagtail.org/en/latest/releases/upgrading.html#compatible-django-python-versions) by Wagtail (for the Wagtail versions as defined above).

### Browser support

We align our browser support targets with that of Wagtail. Have a look at the [official documentation](http://docs.wagtail.org/en/latest/contributing/developing.html).

## Installation

```
pip install wagtail-bakery
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

Define whether you want to build multiple sites or the default site (see examples for impact on directory output), by default this settings is `False`.

```python
BAKERY_MULTISITE = True
```

Add the build directory where you want to be the site be built as flat files.

```python
BUILD_DIR = '/tmp/build/'
```

As you may know with Django bakery, the trickiest part is to make your current models/pages buildable with [Buildable views](https://django-bakery.readthedocs.io/en/latest/buildableviews.html). As Django Wagtail uses only the `Page` model at their lowest level, you can use at least one of the already present Buildable views provided by Wagtail bakery.

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

To build static JSON files representing your site's API, use the following views:

```python
BAKERY_VIEWS = (
	'wagtailbakery.api_views.PagesAPIDetailView',
	'wagtailbakery.api_views.PagesAPIListingView',
	'wagtailbakery.api_views.TypedPagesAPIListingView',
)
```

The API views use Wagtail's V2 API module. To configure the data that is rendered by these views, please refer to Wagtail's [V2 API configuration guide](http://docs.wagtail.org/en/latest/advanced_topics/api/v2/configuration.html).

## Usage

Build the site out as flat files by running the `build` management command.

```
manage.py build
```

If you want to check how your static website will look, use the `buildserver` command after you have build your static files once.

```
manage.py buildserver
```

## Examples

In the [examples](https://github.com/wagtail-nest/wagtail-bakery/tree/main/examples) directory you can find a Wagtail setup with fixtures for a single site as well as a multisite setup.

Create a virtualenv and go to one of the examples, you can use the `Make` command to install all requirements, load fixtures and run the server.

As described in the usage section, use `manage.py build` to build out the example as static files.

**Build output with `BAKERY_MULTISITE=True`**:

```
build/example.com/index.html
build/example.com/about/index.html
build/example.com/blog/index.html
build/example.com/blog/example/index.html
build/static/
```

**Build output with `BAKERY_MULTISITE=False` (default)**:

```
build/index.html
build/about/index.html
build/blog/index.html
build/blog/example/index.html
build/static/
```

## Troubleshooting

For issues [please submit an issue](https://github.com/wagtail-nest/wagtail-bakery/issues/new) on GitHub.

## Development

### Which version combinations to include in Github Actions test matrix?

In order to keep for CI build time from growing out of control, not all Python/Django/Wagtail combinations will be tested.

Test as follow:

- All supported Django/Wagtail combinations with the latest supported Python version.
- The latest supported Django/Wagtail combination for the remaining Python versions.

### Releases

1. Create a new branch (e.g. `release/1.1.3`) for the release of the new version.
1. Update the version number in `pyproject.toml` following [Semantic Versioning](http://semver.org/spec/v2.0.0.html).
1. Update `CHANGELOG.md`.
1. On GitHub, create a pull request and squash merge it.
1. On GitHub, if this is a minor release bump (for example `1.1.0` or `1.2.0` but not `1.1.1`, `1.2.3`), create a `stable/1.1.x` branch from `main`.
1. (Optional) Publish to TestPyPI if you need to verify anything:
   1. Create and push a tag following the pattern `X.Y.Z.devN` (for example `1.1.3.dev1`).
   1. Follow the action progress for the [Publish to TestPyPI](https://github.com/wagtail-nest/wagtail-bakery/actions/workflows/publish-test.yml) workflow.
   1. Check the result on [TestPyPI: wagtail-bakery](https://test.pypi.org/project/wagtail-bakery/).
1. Publish to PyPI:
   1. Create and push a tag following [PEP 440 – Version Identification Specification](https://peps.python.org/pep-0440/) (for example `1.1.3` or `1.1.3rc1`), except for the `.devN` suffix used for testing (see _Publish to TestPyPI_ step above)
   1. Follow the action progress for the [Publish to PyPI](https://github.com/wagtail-nest/wagtail-bakery/actions/workflows/publish.yml) workflow
   1. Check the result on [PyPI: wagtail-bakery](https://pypi.org/project/wagtail-bakery/)
1. On GitHub, create a release and a tag for the new version.

## Credits

`wagtail-bakery` was originally developed by [Rob Moorman](https://github.com/robmoorman) and is now maintained by the Wagtail Nest team.

Thanks to [@mhnbcu](https://github.com/mhnbcu/wagtailbakery) for bringing this
idea up initially, and [Django Bakery](https://github.com/datadesk/django-bakery)
for providing the initial bakery package.

Thanks to all the [contributors](https://github.com/wagtail-nest/wagtail-bakery/graphs/contributors) for their help.
