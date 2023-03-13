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

    # /first
    first_page = PageFactory(depth=3, path='000100010001', slug='first', numchild=2)

    # /first/first
    PageFactory(depth=4, path=f'{first_page.path}0001', slug='first')
    # /first/second
    PageFactory(depth=4, path=f'{first_page.path}0002', slug='second')

    # /second
    PageFactory(depth=3, path='000100010002', slug='second')

    # /third
    PageFactory(depth=3, path='000100010003', slug='third')

    # /unicode-children
    unicode_page = PageFactory(depth=3, path='000100010004', slug='unicode-children', numchild=3)
    # /unicode-children/latin-capital-letter-i-with-diaeresis-Ï
    PageFactory(depth=4, path=f'{unicode_page.path}0001', slug='latin-capital-letter-i-with-diaeresis-Ï')
    # /unicode-children/cyrillic-capital-letter-ya-Я
    PageFactory(depth=4, path=f'{unicode_page.path}0002', slug='cyrillic-capital-letter-ya-Я')
    # /unicode-children/cjk-fire-火
    PageFactory(depth=4, path=f'{unicode_page.path}0003', slug='cjk-fire-火')

    page.numchild = 4
    page.save()

    return page


@pytest.fixture
def multisite(site):
    from tests.factories.page import PageFactory
    from tests.factories.site import SiteFactory

    page_2 = PageFactory(path='00010003', slug='page-2')
    site_2 = SiteFactory(
        hostname='site_2', is_default_site=False, root_page=page_2)

    page_3 = PageFactory(path='00010004', slug='page-3')
    site_3 = SiteFactory(
        hostname='site_3', is_default_site=False, root_page=page_3)

    page_4 = PageFactory(path='00010005', slug='page-4')
    site_4 = SiteFactory(
        hostname='site_4', is_default_site=False, root_page=page_4)

    return [site, site_2, site_3, site_4]
