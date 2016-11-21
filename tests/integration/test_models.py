import pytest


@pytest.mark.django_db
def test_page(page):
    # Test if local url is returned when a single site is used
    assert page.url == '/'


@pytest.mark.django_db
def test_site(site):
    assert site.is_default_site
    assert site.hostname == 'localhost'


@pytest.mark.django_db
def test_page_tree(page_tree):
    descendants = page_tree.get_descendants()
    assert descendants.count() == 3

    # Test if descendants of homepage return correct urls
    assert descendants[0].url == '/first/'
    assert descendants[1].url == '/second/'
    assert descendants[2].url == '/third/'


@pytest.mark.django_db
def test_multisite(multisite):
    assert len(multisite) == 3

    # Test if full urls are returned when multiple sites are used
    assert multisite[0].root_page.url == 'http://site_1/'
    assert multisite[1].root_page.url == 'http://site_2/'
    assert multisite[2].root_page.url == 'http://site_3/'
