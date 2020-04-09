# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import hashlib
import random
from datetime import timedelta

from django.utils import timezone

from jobIT.models import JobOffert

hashed_items_db = JobOffert.objects.filter(still_active = True)
hashed_list=[item.hash_id for item in hashed_items_db]

class ScraperPipeline(object):

    def create_hash(self, *args):
        m = hashlib.md5()
        for arg in args:
            m.update(str(arg).replace("\n", "").encode('utf-8'))

        data = m.hexdigest()
        return data

    def process_item(self, item, spider):
        args = item['title'] + item['price_range'] + item['company'] + item['city']
        for k in item['keywords']:
            args = args + k
        hash_id = self.create_hash(args)
        item['hash_id'] = hash_id
        if hash_id not in hashed_list:
            item.save()
        else:
            hashed_list.remove(hash_id)
        return item

print('hashed list to:',  hashed_list)

for hash_item in hashed_list:
    obj = JobOffert.objects.filter(hash_id=hash_item)
    obj.still_active = False
    obj.end_date = timezone.now() - timedelta(days=1)



