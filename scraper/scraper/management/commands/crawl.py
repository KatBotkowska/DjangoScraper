from django.core.management.base import BaseCommand
from scraper.scraper.spiders import job_offert_scrapper
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

class Command(BaseCommand):
    help = "Release the spider"

    def handle(self, *args, **options):
        process = CrawlerProcess(get_project_settings())
        process.crawl(job_offert_scrapper.JjcrawlerSpider)
        process.start()