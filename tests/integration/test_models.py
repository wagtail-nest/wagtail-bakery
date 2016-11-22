import pytest


@pytest.mark.django_db
def test_page(page):
    # Check if local url is returned when a single site is used
    assert page.url == '/'


@pytest.mark.django_db
def test_site(site):
    assert site.is_default_site
    assert site.hostname == 'localhost'


@pytest.mark.django_db
def test_page_tree(page_tree):
    children = page_tree.get_children()
    assert children.count() == 3

    # Check if children of homepage return correct urls
    assert children[0].url == '/first/'
    assert children[1].url == '/second/'
    assert children[2].url == '/third/'

    children = children[0].get_children()
    assert children.count() == 2

    # Check if children of first child return correct urls
    assert children[0].url == '/first/first/'
    assert children[1].url == '/first/second/'


@pytest.mark.django_db
def test_multisite(multisite):
    assert len(multisite) == 4

    # Check if full urls are returned when multiple sites are used
    assert multisite[0].root_page.url == 'http://localhost/'
    assert multisite[1].root_page.url == 'http://site_2/'
    assert multisite[2].root_page.url == 'http://site_3/'
    assert multisite[3].root_page.url == 'http://site_4/'
