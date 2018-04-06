from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel


class AbstractExamplePage(Page):
    body = StreamField([
        ('paragraph', blocks.RichTextBlock())
    ])

    content_panels = [
        FieldPanel('title'),
        StreamFieldPanel('body')
    ]

    class Meta:
        abstract = True


class HomePage(AbstractExamplePage):
    pass


class GenericPage(AbstractExamplePage):
    pass


class BlogListPage(AbstractExamplePage):
    pass


class BlogPostPage(AbstractExamplePage):
    pass
