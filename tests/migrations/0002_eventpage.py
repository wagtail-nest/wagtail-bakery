# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-11 08:04
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail
from wagtail.contrib.routable_page.models import RoutablePageMixin


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0032_add_bulk_delete_page_permission'),
        ('tests', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=(RoutablePageMixin, 'wagtailcore.page'),
        ),
    ]
