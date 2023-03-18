import factory
from wagtail.models import Page


class PageFactory(factory.DjangoModelFactory):
    depth = 2
    numchild = 0
    path = '00010002'
    title = 'Page'
    slug = 'page'
    url_path = '/page/'

    class Meta:
        model = Page
