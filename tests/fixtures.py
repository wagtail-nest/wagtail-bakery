import pytest

from wagtail.wagtailcore.models import Page, Site

from tests.factories.page import PageFactory
from tests.factories.site import SiteFactory


@pytest.fixture
def page():
    page = Page.objects.get(slug='home')
    return page


@pytest.fixture
def site():
    site = Site.objects.get(is_default_site=True)
    return site


@pytest.fixture
def page_tree(page):
    child_1 = PageFactory(depth=3, path='000100010001', slug='first')
    child_2 = PageFactory(depth=3, path='000100010002', slug='second')
    child_3 = PageFactory(depth=3, path='000100010003', slug='third')
    return page


@pytest.fixture
def multisite(site):
    page_1 = PageFactory(path='00010003', slug='page-1')
    site_1 = SiteFactory(
        hostname='site_1', is_default_site=False, root_page=page_1)

    page_2 = PageFactory(path='00010004', slug='page-2')
    site_2 = SiteFactory(
        hostname='site_2', is_default_site=False, root_page=page_2)

    page_3 = PageFactory(path='00010005', slug='page-3')
    site_3 = SiteFactory(
        hostname='site_3', is_default_site=False, root_page=page_3)

    return [site_1, site_2, site_3]
