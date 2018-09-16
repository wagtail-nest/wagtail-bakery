import factory
import wagtail
if wagtail.VERSION >= (2, 0):
    from wagtail.core.models import Page
else:
    from wagtail.wagtailcore.models import Page


class PageFactory(factory.DjangoModelFactory):
    depth = 2
    numchild = 0
    path = '00010002'
    title = 'Page'
    slug = 'page'
    url_path = '/page/'

    class Meta:
        model = Page
