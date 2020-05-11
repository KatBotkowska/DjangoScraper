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

# def hashed_list():
#     hashed_items_db = JobOffert.objects.filter(still_active = True)
#     hashed_list=[item.hash_id for item in hashed_items_db]
#     return hashed_list

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
        #item['hash_id'] = hash_id
        if hash_id not in hashed_list:
            item['hash_id'] = hash_id
            #item['scrapped'] = True
            item.save()
        else:
            hashed_list.remove(hash_id)
            item = JobOffert.objects.get(hash_id=hash_id)
            item['scrapped'] = True
            item.save()
        return item


    def close_spider(self, spider):
        not_active_items=JobOffert.objects.filter(scrapped=False)
        for item in not_active_items:
            item.still_active = False
            item.end_date = timezone.now() - timedelta(days=1)
            item.save()
        active_items=JobOffert.objects.filter(scrapped=True)
        for item in active_items:
            item.scrapped = False
            item.save()
        return item

        # for hash_item in hashed_list:
        #     obj = JobOffert.objects.get(hash_id=hash_item)
        #     obj.still_active = False
        #     obj.end_date = timezone.now() - timedelta(days=1)
        #     obj.save()
        # return hashed_list


