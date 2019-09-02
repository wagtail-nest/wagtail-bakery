from django.shortcuts import redirect, render
import wagtail
if wagtail.VERSION >= (2, 0):
    from wagtail.contrib.routable_page.models import RoutablePageMixin, route
    from wagtail.core.models import Page
else:
    from wagtail.contrib.wagtailroutablepage.models import RoutablePageMixin, route
    from wagtail.wagtailcore.models import Page


class RedirectPage(Page):
    def serve(self, request, *args, **kwargs):
        return redirect('http://www.example.com/')


class EventPage(RoutablePageMixin, Page):
    @route(r'^$')
    def current_events(self, request):
        return render(request, 'current_events.html', {
            'page': self,
        })

    @route(r'^year/(\d+)/$')
    @route(r'^year/current/$')
    def events_for_year(self, request, year=None):
        return render(request, 'events_for_year.html', {
            'page': self,
            'year': year,
        })

    def get_static_site_paths(self):
        return super(EventPage, self).get_static_site_paths()

    @property
    def url(self):
        return '/eventpage/{}'.format(self.slug)
