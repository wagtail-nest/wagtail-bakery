import os

import pytest
from django.conf import settings
from django.core import management

from tests.models import EventPage


@pytest.mark.django_db
def test_page_has_multiple_routes(site):
    redirect_page = EventPage.objects.create(
        depth=1,
        path='0002',
        title='Page',
        slug='page',
    )

    # Make event page the root page
    site.root_page = redirect_page
    site.save()

    # Build static files
    management.call_command('build', '--skip-static', '--skip-media')
    assert os.path.exists(os.path.join(settings.BUILD_DIR, 'eventpage', 'page', 'index.html'))
