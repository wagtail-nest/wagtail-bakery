# Getting started

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

If you want to check how your static website will look like, use the `buildserver` command after you have build your static files once.

```
manage.py buildserver
```

Please see the documentation at [https://wagtail-bakery.readthedocs.io](https://wagtail-bakery.readthedocs.io) for more information how to use Django bakery.

## Examples

In the [examples](https://github.com/moorinteractive/wagtail-bakery/tree/master/examples) directory you can find a Wagtail setup with fixtures for a single site as well as a multisite setup.

Create a virtualenv and go to one of the examples, you can use the `Make` command to install all requirements, load fixtures and run the server.

Use as described in the usage section `manage.py build` to build the example out as static files.
