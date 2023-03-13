import pytest
from django.conf import settings

from wagtailbakery.views import AllPagesView, AllPublishedPagesView, WagtailBakeryView


@pytest.mark.django_db
def test_wagtail_bakery_view_get_url(page_tree):
    view = WagtailBakeryView()

    # Check url for homepage
    url = view.get_url(page_tree)
    assert url == '/'

    # Check child url for first child page
    child_page = page_tree.get_descendants().first()
    url = view.get_url(child_page)
    assert url == '/first/'

    # Check child url of the first grandchild page
    child_page = child_page.get_descendants().first()
    url = view.get_url(child_page)
    assert url == '/first/first/'


@pytest.mark.django_db
def test_wagtail_bakery_view_build_path(page_tree):
    view = WagtailBakeryView()

    # Check build path for homepage
    build_path = view.get_build_path(page_tree)
    assert build_path == settings.BUILD_DIR + '/index.html'

    # Check build path for first child page
    child_page = page_tree.get_children().first()
    build_path = view.get_build_path(child_page)
    assert build_path == settings.BUILD_DIR + '/first/index.html'

    # Check build path of the first grandchild page
    grandchild_page = child_page.get_children().first()
    build_path = view.get_build_path(grandchild_page)
    assert build_path == settings.BUILD_DIR + '/first/first/index.html'

    # Check build path for unicode-children child page
    child_page = page_tree.get_children().last()
    build_path = view.get_build_path(child_page)
    assert build_path == settings.BUILD_DIR + '/unicode-children/index.html'

    # Check build path for unicode-children grandchild pages
    grandchild_pages = child_page.get_children().all()

    build_path = view.get_build_path(grandchild_pages[0])
    assert build_path == (
        settings.BUILD_DIR + '/unicode-children/latin-capital-letter-i-with-diaeresis-Ï/index.html'
    )

    build_path = view.get_build_path(grandchild_pages[1])
    assert build_path == (
        settings.BUILD_DIR + '/unicode-children/cyrillic-capital-letter-ya-Я/index.html'
    )

    build_path = view.get_build_path(grandchild_pages[2])
    assert build_path == settings.BUILD_DIR + '/unicode-children/cjk-fire-火/index.html'


@pytest.mark.django_db
def test_wagtail_bakery_view_build_path_for_multisite(multisite):
    view = WagtailBakeryView()
    site = multisite[0]
    page = site.root_page

    # Check build path for homepage
    build_path = view.get_build_path(page)
    assert build_path == '%s/index.html' % (
        settings.BUILD_DIR)


@pytest.mark.django_db
def test_all_published_pages_for_single_page(page):
    view = AllPublishedPagesView()
    qs = view.get_queryset()

    # Check if published page is returned
    assert qs.filter(id=page.id).exists()

    # Check if there are no unpublished pages returned
    page.live = False
    page.save()
    assert not qs.filter(live=False).exists()
    assert not qs.filter(id=page.id).exists()


@pytest.mark.django_db
def test_all_published_pages_for_multiple_pages(page_tree):
    view = AllPublishedPagesView()
    qs = view.get_queryset()

    # Check if all pages in page tree are returned
    assert qs.count() == 10


@pytest.mark.django_db
def test_all_pages_for_single_page(page):
    view = AllPagesView()
    qs = view.get_queryset()

    # Check if published page is returned
    assert qs.filter(id=page.id).exists()

    # Check if there are still unpublished pages returned
    page.live = False
    page.save()
    assert qs.filter(live=False).exists()
    assert qs.filter(id=page.id).exists()
