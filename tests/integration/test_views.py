import pytest

from wagtailbakery.views import AllPublishedPagesView, WagtailBakeryView


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

    # Check child url of the first child page
    child_page = child_page.get_descendants().first()
    url = view.get_url(child_page)
    assert url == '/first/first/'


@pytest.mark.django_db
def test_all_published_pages(page):
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
def test_get_build_path(page):
    # view = AllPublishedPagesView
    pass
