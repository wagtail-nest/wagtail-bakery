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
    assert children.count() == 4

    # Check if children of homepage return correct urls
    assert children[0].url == '/first/'
    assert children[1].url == '/second/'
    assert children[2].url == '/third/'
    assert children[3].url == '/unicode-children/'

    # Check if children of first child return correct urls
    grandchildren = children[0].get_children()
    assert grandchildren.count() == 2
    assert grandchildren[0].url == '/first/first/'
    assert grandchildren[1].url == '/first/second/'

    # Check if children of unicode-children return correct urls
    grandchildren = children[3].get_children()
    assert grandchildren.count() == 3

    # Unicode characters are URL-encoded with `url` but not `url_path`.
    # However manual testing shows that the page is indeed accessible with the non-encoded string.
    assert grandchildren[0].url_path == (
        '/home/unicode-children/latin-capital-letter-i-with-diaeresis-Ï/'
    )
    assert grandchildren[1].url_path == '/home/unicode-children/cyrillic-capital-letter-ya-Я/'
    assert grandchildren[2].url_path == '/home/unicode-children/cjk-fire-火/'


@pytest.mark.django_db
def test_multisite(multisite):
    assert len(multisite) == 4

    # Check if full urls are returned when multiple sites are used
    assert multisite[0].root_page.url == 'http://localhost/'
    assert multisite[1].root_page.url == 'http://site_2/'
    assert multisite[2].root_page.url == 'http://site_3/'
    assert multisite[3].root_page.url == 'http://site_4/'
