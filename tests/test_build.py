import os

from django.core.management import call_command


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def test_build_command():
    # Build static site
    call_command('build')

    # Read build directory
    assert os.path.exists(os.path.join(BASE_DIR, 'build'))
