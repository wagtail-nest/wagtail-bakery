import pytest


@pytest.fixture
def page():
    from wagtail.core.models import Page
    return Page.objects.get(slug='home')


@pytest.fixture
def site():
    from wagtail.core.models import Site
    return Site.objects.get(is_default_site=True)


@pytest.fixture
def page_tree(page):
    from tests.factories.page import PageFactory

    PageFactory(depth=3, path='000100010001', slug='first', numchild=2)
    PageFactory(depth=3, path='000100010002', slug='second')
    PageFactory(depth=3, path='000100010003', slug='third')

    PageFactory(depth=4, path='0001000100010001', slug='first')
    PageFactory(depth=4, path='0001000100010002', slug='second')

    page.numchild = 3
    page.save()

    return page


@pytest.fixture
def multisite(site):
    from tests.factories.page import PageFactory
    from tests.factories.site import SiteFactory

    page_2 = PageFactory(path='00010003', slug='page-2')
    site_2 = SiteFactory(
        hostname='site2', is_default_site=False, root_page=page_2)

    page_3 = PageFactory(path='00010004', slug='page-3')
    site_3 = SiteFactory(
        hostname='site3', is_default_site=False, root_page=page_3)

    page_4 = PageFactory(path='00010005', slug='page-4')
    site_4 = SiteFactory(
        hostname='site4', is_default_site=False, root_page=page_4)

    return [site, site_2, site_3, site_4]
