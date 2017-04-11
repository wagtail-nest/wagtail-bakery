import os

import pytest
from django.conf import settings
from django.core import management

from tests.models import RedirectPage


@pytest.mark.django_db
def test_page_has_redirect_response(site):
    redirect_page = RedirectPage.objects.create(
        depth=1,
        path='0002',
        title='Page',
        slug='page',
    )

    # Make redirect page the root page
    site.root_page = redirect_page
    site.save()

    # Build static files
    management.call_command('build', '--skip-static', '--skip-media')
    assert os.path.exists(os.path.join(settings.BUILD_DIR, 'index.html'))

    # Check if meta tag is present
    content = open(os.path.join(settings.BUILD_DIR, 'index.html')).read()
    assert '<meta http-equiv="refresh" content="1; url=http://www.example.com/">' in content # noqa
