# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy_djangoitem import DjangoItem
from jobIT.models import JobOffert


class JobOffertItem(DjangoItem):
    django_model = JobOffert

