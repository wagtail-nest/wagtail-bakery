from django.shortcuts import redirect
from wagtail.wagtailcore.models import Page


class RedirectPage(Page):
    def serve(self, request, *args, **kwargs):
        return redirect('http://www.example.com/')
