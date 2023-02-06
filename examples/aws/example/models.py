from wagtail import blocks
from wagtail.admin.panels import FieldPanel
from wagtail.admin.panels import FieldPanel as StreamFieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page

from wagtailbakery.models import AutoPublishingWagtailBakeryModel


class AbstractExamplePage(Page, AutoPublishingWagtailBakeryModel):
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
